"""PE screening: build validated alkane topologies, prepare, run, and inspect MD.

Run under Linux/WSL with GROMACS, numpy and RDKit. No fitted parameters are
invented: bonded/nonbonded values are resolved from the archived CHARMM port.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent


def save_json(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2) + "\n")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def config():
    return json.loads((ROOT / 'screening.json').read_text())


def call(args, cwd, log, stdin=None):
    with (Path(cwd) / log).open('a') as f:
        f.write('\nCOMMAND: ' + repr([str(x) for x in args]) + '\n')
        f.flush()
        subprocess.run([str(x) for x in args], cwd=cwd, input=stdin,
                       text=True, stdout=f, stderr=subprocess.STDOUT, check=True)


def verify_ff(ff):
    """Fail closed if the propane reference differs from our alkane template."""
    import re
    text = (ff / 'cgenff.rtp').read_text()
    block = text.split('[ PRPA ]')[1].split('[ PRPE ]')[0]
    for name, typ, q in [('C1', 'CG331', -.27), ('C2', 'CG321', -.18),
                         ('H11', 'HGA3', .09), ('H21', 'HGA2', .09)]:
        match = re.search(r'^\s*' + name + r'\s+(\w+)\s+([-\d.]+)', block, re.M)
        if not match or match[1] != typ or abs(float(match[2]) - q) > 1e-8:
            raise ValueError('Unsupported CGenFF alkane reference: ' + name)
    return {p.name: digest(p) for p in sorted(ff.iterdir()) if p.is_file()}


def molecule(ncarbon):
    from rdkit import Chem
    return Chem.AddHs(Chem.MolFromSmiles('C' * ncarbon))


def topology(mol):
    """Linear saturated alkane only; enumerate bonded terms and 1-4 pairs."""
    neighbors = {a.GetIdx(): [b.GetIdx() for b in a.GetNeighbors()] for a in mol.GetAtoms()}
    names, types, charges = [], [], []
    nc = sum(a.GetAtomicNum() == 6 for a in mol.GetAtoms())
    for a in mol.GetAtoms():
        i = a.GetIdx()
        if a.GetAtomicNum() == 6:
            terminal = sum(mol.GetAtomWithIdx(j).GetAtomicNum() == 6 for j in neighbors[i]) == 1
            names.append('C' + str(i + 1))
            types.append('CG331' if terminal else 'CG321')
            charges.append(-.27 if terminal else -.18)
        else:
            parent = mol.GetAtomWithIdx(neighbors[i][0])
            terminal = sum(n.GetAtomicNum() == 6 for n in parent.GetNeighbors()) == 1
            names.append('H' + str(i - nc + 1))
            types.append('HGA3' if terminal else 'HGA2')
            charges.append(.09)
    assert abs(sum(charges)) < 1e-8
    bonds = sorted(tuple(sorted((b.GetBeginAtomIdx(), b.GetEndAtomIdx()))) for b in mol.GetBonds())
    angles = [(i, j, k) for j in neighbors for i, k in itertools.combinations(sorted(neighbors[j]), 2)]
    torsions = [(i, j, k, l) for j, k in bonds for i in neighbors[j] if i != k
                for l in neighbors[k] if l != j]
    pairs = sorted(set(tuple(sorted((i, l))) for i, j, k, l in torsions))
    lines = ['; PE alkane template from official CGenFF PRPA types/charges', '[ moleculetype ]',
             'PE 3', '[ atoms ]']
    for i, a in enumerate(mol.GetAtoms()):
        lines.append(f'{i+1} {types[i]} 1 PE {names[i]} {i+1} {charges[i]:.6f} {a.GetMass():.5f}')
    for title, entries, fun in [('bonds', bonds, 1), ('pairs', pairs, 1),
                                 ('angles', angles, 5), ('dihedrals', torsions, 9)]:
        lines.append(f'[ {title} ]')
        lines.extend(' '.join(str(i+1) for i in row) + f' {fun}' for row in entries)
    lines += ['#ifdef POSRES', '[ position_restraints ]']
    lines.extend(f'{i+1} 1 1000 1000 1000' for i in range(nc))
    lines.append('#endif')
    return '\n'.join(lines) + '\n', names


def carbon_walk(n, rng):
    import numpy as np
    theta = np.deg2rad(112.)
    for attempt in range(200):
        points = [np.array([0., 0., 0.]), np.array([1.53, 0., 0.]),
                  np.array([1.53-1.53*np.cos(theta), 1.53*np.sin(theta), 0.])]
        for k in range(3, n):
            a, b, c = points[-3:]
            u = (c-b)/np.linalg.norm(c-b)
            v = np.cross(b-a, u); v /= np.linalg.norm(v)
            w = np.cross(v, u)
            accepted = False
            for trial in range(20):
                phi = np.deg2rad(rng.choice([180., 60., -60.]) + rng.normal(0, 6))
                p = c + 1.53*(-np.cos(theta)*u + np.sin(theta)*(np.cos(phi)*w + np.sin(phi)*v))
                if np.min(np.linalg.norm(np.array(points[:-2])-p, axis=1)) > 2.8:
                    points.append(p); accepted = True; break
            if not accepted:
                break
        if len(points) == n:
            return np.array(points)
    raise RuntimeError('Could not build a self-avoiding chain')


def conformers(n, count, seed):
    import numpy as np
    from rdkit import Chem
    from rdkit.Chem import AllChem, rdMolTransforms
    rng = np.random.default_rng(seed)
    result = []
    for k in range(count):
        m = Chem.MolFromSmiles('C'*n)
        xyz = carbon_walk(n, rng)
        conf = Chem.Conformer(n)
        for i, p in enumerate(xyz):
            conf.SetAtomPosition(i, p.tolist())
        m.AddConformer(conf)
        m = Chem.AddHs(m, addCoords=True)
        # Geometry cleanup only. This gas-phase optimization is not reference MD.
        AllChem.MMFFOptimizeMolecule(m, maxIters=100)
        pos = np.array(m.GetConformer().GetPositions())
        c = pos[:n] - pos[:n].mean(axis=0)
        rg = float(np.sqrt((c*c).sum()/n)/10)
        trans = float(np.mean([abs(rdMolTransforms.GetDihedralDeg(m.GetConformer(),i,i+1,i+2,i+3)) > 150 for i in range(n-3)]))
        result.append((rg, trans, pos))
    return result


def write_pdb(path, pos, names, nc):
    lines = []
    for i, (p, name) in enumerate(zip(pos, names), 1):
        element = 'C' if i <= nc else 'H'
        lines.append(f'ATOM  {i:5d} {name:>4s}  PE A   1    {p[0]:8.3f}{p[1]:8.3f}{p[2]:8.3f}  1.00  0.00          {element:>2s}')
    Path(path).write_text('\n'.join(lines) + '\nEND\n')


def mdp(stage, seed, production_ns, smoke=False):
    common = dict(cutoff_scheme='Verlet', nstlist=20, rlist=1.2,
                  coulombtype='PME', rcoulomb=1.2, vdwtype='Cut-off',
                  vdw_modifier='Force-switch', rvdw_switch=1.0, rvdw=1.2,
                  DispCorr='no', pbc='xyz', constraints='h-bonds',
                  constraint_algorithm='lincs', lincs_order=4)
    if stage == 'em':
        common.update(integrator='steep', nsteps=50000, emtol=500, emstep=.001,
                      constraints='none')
    else:
        steps = {'nvt':250000, 'npt':2500000, 'relax':500000,
                 'prod':int(production_ns*500000)}
        if smoke:
            steps = dict(nvt=500, npt=500, relax=500, prod=1000)
        common.update(integrator='md', dt=.002, nsteps=steps[stage],
                      tcoupl='v-rescale', tc_grps='System', tau_t=2.0, ref_t=300,
                      nstcomm=100, comm_mode='Linear', nstcalcenergy=100,
                      nstenergy=500, nstlog=500, nstxout=0, nstvout=0, nstfout=0,
                      nstxout_compressed=500, compressed_x_grps='System',
                      continuation='no' if stage=='nvt' else 'yes',
                      gen_vel='yes' if stage=='nvt' else 'no', ld_seed=seed)
        if stage == 'nvt':
            common.update(define='-DPOSRES', gen_temp=300, gen_seed=seed)
        if stage == 'npt':
            common.update(pcoupl='C-rescale', pcoupltype='isotropic', tau_p=5,
                          ref_p=1, compressibility=4.5e-5)
        else:
            common['pcoupl'] = 'no'
    return '\n'.join(f'{k.replace("_", "-")} = {v}' for k,v in common.items()) + '\n'


def build(args):
    import numpy as np
    cfg = config(); ff = ROOT / cfg['forcefield']
    if cfg['temperature_K'] != 300:
        raise ValueError('This pilot is fixed at 300 K; change the protocol and tests before varying temperature')
    hashes = verify_ff(ff)
    out = ROOT / args.output
    if (out / 'manifest.json').exists():
        raise FileExistsError('Existing manifest: use another --output; never overwrite runs')
    out.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ff, out / ff.name, dirs_exist_ok=True)
    manifest = dict(config=cfg, smoke=args.smoke, forcefield_sha256=hashes,
                    generator_sha256=digest(__file__), replicates=[])
    for system, spec in cfg['systems'].items():
        n = 2*spec['repeat_units']
        mol = molecule(n); itp, names = topology(mol)
        candidates = conformers(n, args.candidates, cfg['base_seed']+n)
        candidates.sort(key=lambda x: x[0])
        classes = ['compact', 'ordered', 'expanded']
        for rep in range(spec['replicates']):
            cls = classes[rep % 3]
            if cls == 'compact':
                selected = candidates.pop(0)
            elif cls == 'expanded':
                selected = candidates.pop(-1)
            else:
                j = max(range(max(1,len(candidates)//2)), key=lambda j:candidates[j][1])
                selected = candidates.pop(j)
            rg, order, pos = selected
            folder = out / system / f'rep{rep+1:02d}'; folder.mkdir(parents=True)
            write_pdb(folder/'polymer.pdb', pos, names, n)
            (folder/'pe.itp').write_text(itp)
            (folder/'topol.top').write_text(f'#include "../../{ff.name}/forcefield.itp"\n#include "pe.itp"\n#include "../../{ff.name}/tip3p.itp"\n[ system ]\n{system} in water\n[ molecules ]\nPE 1\n')
            seed = cfg['base_seed'] + n*100 + rep
            for stage in ['em','nvt','npt','relax','prod']:
                (folder/f'{stage}.mdp').write_text(mdp(stage, seed, spec['production_ns'], args.smoke))
            box = max(cfg['box_nm'], float(np.ptp(pos, axis=0).max()/10 + 3.0))
            info = dict(system=system, replicate=rep+1, seed=seed, preparation=cls,
                        initial_rg_nm=rg, initial_trans_fraction=order, ncarbon=n,
                        box_nm=box, production_ns=spec['production_ns'],
                        relative_path=str(folder.relative_to(out)), atom_names=names)
            save_json(folder/'metadata.json', info)
            manifest['replicates'].append(info)
    # Match box sizes within each chain length to avoid preparation confounding.
    for system in cfg['systems']:
        entries = [x for x in manifest['replicates'] if x['system']==system]
        box = max(x['box_nm'] for x in entries)
        for entry in entries:
            entry['box_nm'] = box
            save_json(out/entry['relative_path']/'metadata.json', entry)
    save_json(out/'manifest.json', manifest)
    print(f'Built {len(manifest["replicates"])} replicas in {out}')


def run(args):
    folder = Path(args.replica).resolve()
    info = json.loads((folder/'metadata.json').read_text())
    gmx = args.gmx
    if not shutil.which(gmx):
        raise RuntimeError('GROMACS executable not found: '+gmx)
    engine_info=dict(path=str(Path(shutil.which(gmx)).resolve()),
                     executable_sha256=digest(Path(shutil.which(gmx)).resolve()))
    engine_file=folder/'engine.json'
    if engine_file.exists() and json.loads(engine_file.read_text()) != engine_info:
        raise RuntimeError('GROMACS executable changed: use a fresh run tree')
    if not engine_file.exists(): save_json(engine_file,engine_info)
    root=folder.parent.parent
    manifest=json.loads((root/'manifest.json').read_text())
    ff=root/Path(manifest['config']['forcefield']).name
    for name,expected in manifest['forcefield_sha256'].items():
        if digest(ff/name)!=expected:
            raise RuntimeError('Force-field file changed: '+name)
    call([gmx,'--version'], folder, 'gromacs-version.txt')
    lock = folder/'RUNNING'
    try:
        inputs = {p.name:digest(p) for p in [folder/'polymer.pdb',folder/'pe.itp',
                  *[folder/f'{s}.mdp' for s in ['em','nvt','npt','relax','prod']]]}
        frozen=folder/'input_hashes.json'
        if frozen.exists() and json.loads(frozen.read_text()) != inputs:
            raise RuntimeError('Inputs changed after execution began. Use a new output tree.')
        if not frozen.exists(): save_json(frozen,inputs)
        fd = os.open(lock, os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:
        raise RuntimeError('RUNNING lock exists; check process before removing it')
    os.write(fd, f'{os.getpid()}\n'.encode()); os.close(fd)
    try:
        if not (folder/'prepared.json').exists():
            # Recover from interrupted solvation without duplicating SOL counts.
            top = (folder/'topol.top').read_text()
            (folder/'topol.top').write_text('\n'.join(l for l in top.splitlines() if not l.strip().startswith('SOL '))+'\n')
            call([gmx,'editconf','-f','polymer.pdb','-o','boxed.gro','-c','-bt','cubic',
                  '-box', *[str(info['box_nm'])]*3],folder,'prepare.log')
            call([gmx,'solvate','-cp','boxed.gro','-cs','spc216.gro','-o','solvated.gro','-p','topol.top'],folder,'prepare.log')
            save_json(folder/'prepared.json',dict(topology_sha256=digest(folder/'topol.top')))
        elif json.loads((folder/'prepared.json').read_text())['topology_sha256'] != digest(folder/'topol.top'):
            raise RuntimeError('Solvated topology changed after preparation')
        if args.until == 'prepare':
            if not (folder/'em.tpr').exists():
                call([gmx,'grompp','-f','em.mdp','-c','solvated.gro','-p','topol.top',
                      '-o','em.tpr','-po','em.resolved.mdp','-pp','em.processed.top'],folder,'em.grompp.log')
            return
        previous = 'solvated'
        for stage in ['em','nvt','npt','relax','prod']:
            done = folder/f'{stage}.done.json'
            if done.exists():
                previous=stage
                if stage==args.until: break
                continue
            command = [gmx,'grompp','-f',f'{stage}.mdp','-c',f'{previous}.gro',
                       '-p','topol.top','-o',f'{stage}.tpr','-po',f'{stage}.resolved.mdp',
                       '-pp',f'{stage}.processed.top']
            if stage=='nvt': command += ['-r',f'{previous}.gro']
            if stage in ['npt','relax','prod']: command += ['-t',f'{previous}.cpt']
            if not (folder/f'{stage}.tpr').exists():
                call(command,folder,f'{stage}.grompp.log')
            command = [gmx,'mdrun','-deffnm',stage,'-ntmpi','1','-ntomp',str(args.threads)]
            if (folder/f'{stage}.cpt').exists(): command += ['-cpi',f'{stage}.cpt','-append']
            if args.maxh: command += ['-maxh',str(args.maxh)]
            call(command,folder,f'{stage}.console.log')
            # mdrun -maxh can return success before the requested end time.
            log = (folder/f'{stage}.log').read_text(errors='replace')
            console = (folder/f'{stage}.console.log').read_text(errors='replace')
            if 'LINCS WARNING' in log+console or 'Fatal error:' in log+console:
                raise RuntimeError('Numerical warning/error: inspect '+stage+' logs before continuing')
            if stage != 'em':
                import re
                pairs = re.findall(r'Step\s+Time\s*\n\s*(\d+)\s+([\d.Ee+-]+)',log)
                required = int(next(l.split('=')[1] for l in (folder/f'{stage}.mdp').read_text().splitlines() if l.startswith('nsteps')))
                if not pairs or int(pairs[-1][0]) < required:
                    print('Checkpointed before completion; rerun same command to resume'); return
            elif 'converged to Fmax' not in log:
                raise RuntimeError('Minimization did not reach the requested Fmax; inspect em.log')
            save_json(done, dict(finished=time.time(), tpr_sha256=digest(folder/f'{stage}.tpr')))
            previous = stage
            if stage==args.until: break
    finally:
        lock.unlink(missing_ok=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    b=sub.add_parser('build'); b.add_argument('--output',default='runs'); b.add_argument('--smoke',action='store_true'); b.add_argument('--candidates',type=int,default=48)
    r=sub.add_parser('run'); r.add_argument('replica'); r.add_argument('--gmx',default='gmx'); r.add_argument('--threads',type=int,default=8); r.add_argument('--maxh',type=float); r.add_argument('--until',choices=['prepare','em','nvt','npt','relax','prod'],default='prod')
    args=parser.parse_args()
    if args.command=='build':
        if args.candidates < 12: parser.error('--candidates must be at least 12')
        build(args)
    else: run(args)


if __name__=='__main__':
    main()
