//! nerve_hom: replay a simplified JSON op list into a homotopy.io `.hom` workspace.
//!
//! Ops (JSON array of objects with an "op" field):
//!   {"op":"zero","name":"U0"}                         create a 0-cell
//!   {"op":"select","gen":[id,dim]}                    load a generator's diagram into the workspace
//!   {"op":"source"} / {"op":"target"}                 SetBoundary; second boundary creates a generator
//!   {"op":"identity"} / {"op":"clear"}
//!   {"op":"attach","gen":[id,dim],"boundary":["Target",0]|null,"embedding":[..]}
//!   {"op":"name","gen":[id,dim],"name":"..."}         rename after construction
//!   {"op":"meta","title":"...","author":"...","abstr":"..."}
//! The attached generator's diagram is taken from the signature, so the caller never has to
//! serialize homotopy.io diagrams by hand.  Written for the pronerv fluid-nerve project.
use std::{collections::HashMap, fs, path::PathBuf};

use anyhow::{anyhow, bail, Context};
use homotopy_core::{
    common::{Boundary, BoundaryPath, Generator},
    signature::Signature as _,
    DiagramN,
};
use homotopy_model::{
    history::Proof,
    proof::{generators::GeneratorInfo, Action, AttachOption, Metadata},
    serialize,
};
use serde_json::Value;

fn gen_of(v: &Value) -> anyhow::Result<Generator> {
    let a = v.as_array().ok_or_else(|| anyhow!("gen must be [id,dim]"))?;
    Ok(Generator::new(a[0].as_u64().unwrap() as usize, a[1].as_u64().unwrap() as usize))
}

fn main() -> anyhow::Result<()> {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        bail!("usage: nerve_hom <ops.json> <out.hom>");
    }
    let ops: Vec<Value> = serde_json::from_slice(&fs::read(&args[1])?)?;
    let out = PathBuf::from(&args[2]);
    let mut proof: Proof = Default::default();
    let mut names: HashMap<Generator, String> = HashMap::new();
    let mut meta = Metadata::new();
    for (k, op) in ops.iter().enumerate() {
        let kind = op["op"].as_str().ok_or_else(|| anyhow!("op {k} lacks 'op'"))?;
        let ctx = || format!("op {k}: {op}");
        match kind {
            "zero" => {
                proof.update(&Action::CreateGeneratorZero).with_context(ctx)?;
                if let Some(n) = op["name"].as_str() {
                    let id = proof.signature.iter().map(|i| i.generator.id).max().unwrap();
                    names.insert(Generator::new(id, 0), n.to_string());
                }
            }
            "select" => {
                proof.update(&Action::SelectGenerator(gen_of(&op["gen"])?)).with_context(ctx)?;
            }
            "source" => {
                proof.update(&Action::SetBoundary(Boundary::Source)).with_context(ctx)?;
            }
            "target" => {
                proof.update(&Action::SetBoundary(Boundary::Target)).with_context(ctx)?;
                if let Some(n) = op["name"].as_str() {
                    // the generator just created has the largest id
                    let info = proof.signature.iter().max_by_key(|i| i.generator.id).unwrap();
                    names.insert(info.generator, n.to_string());
                }
            }
            "identity" => {
                proof.update(&Action::TakeIdentityDiagram).with_context(ctx)?;
            }
            "clear" => {
                proof.update(&Action::ClearWorkspace).with_context(ctx)?;
            }
            "attach" => {
                let g = gen_of(&op["gen"])?;
                let info = proof
                    .signature
                    .generator_info(g)
                    .ok_or_else(|| anyhow!("unknown generator {g:?}"))?;
                let diagram: DiagramN = DiagramN::try_from(info.diagram.clone())
                    .map_err(|_| anyhow!("generator {g:?} has a 0-dimensional diagram"))?;
                let boundary_path = match &op["boundary"] {
                    Value::Null => None,
                    Value::Array(a) => {
                        let b = match a[0].as_str().unwrap_or("Target") {
                            "Source" => Boundary::Source,
                            _ => Boundary::Target,
                        };
                        Some(BoundaryPath(b, a[1].as_u64().unwrap_or(0) as usize))
                    }
                    _ => bail!("bad boundary in op {k}"),
                };
                let embedding: Vec<usize> = op["embedding"]
                    .as_array()
                    .map(|a| a.iter().map(|x| x.as_u64().unwrap() as usize).collect())
                    .unwrap_or_default();
                let option = AttachOption {
                    generator: g,
                    boundary_path,
                    embedding: embedding.into_iter().collect(),
                    tag: None,
                    diagram,
                };
                proof.update(&Action::Attach(option)).with_context(ctx)?;
            }
            "name" => {
                names.insert(gen_of(&op["gen"])?, op["name"].as_str().unwrap_or("").to_string());
            }
            "meta" => {
                meta.title = op["title"].as_str().map(str::to_string);
                meta.author = op["author"].as_str().map(str::to_string);
                meta.abstr = op["abstr"].as_str().map(str::to_string);
            }
            other => bail!("unknown op {other}"),
        }
    }
    proof.signature = proof.signature.filter_map(|info| {
        let mut info: GeneratorInfo = info.clone();
        if let Some(n) = names.get(&info.generator) {
            info.name = n.clone();
        }
        Some(info)
    });
    proof.metadata = meta;
    // Deep-check every generator diagram before writing.
    for g in proof.signature.iter() {
        g.diagram
            .check(true)
            .map_err(|e| anyhow!("deep check failed for {:?}: {:?}", g.generator, e))?;
    }
    let mut counts: HashMap<usize, usize> = HashMap::new();
    for g in proof.signature.iter() {
        *counts.entry(g.generator.dimension).or_default() += 1;
    }
    let data = serialize::serialize(proof.signature.clone(), None, proof.metadata.clone());
    fs::write(&out, &data).context("could not write .hom")?;
    // Round trip.
    serialize::deserialize(&data).ok_or_else(|| anyhow!("round-trip deserialize failed"))?;
    let mut dims: Vec<_> = counts.into_iter().collect();
    dims.sort();
    println!(
        "wrote {} ({} bytes); generators by dimension: {:?}",
        out.display(),
        data.len(),
        dims
    );
    Ok(())
}
