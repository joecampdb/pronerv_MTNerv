"""A local validation report, separate from the legacy exploratory manuscript."""
import json
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'output/robustness';OUT=ROOT.parent/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
full=(SRC/'full-audit.json').exists()
r=json.loads((SRC/('full-audit.json' if full else 'subset-audit.json')).read_text())
a=r['systems']['alanine'];c=r['systems']['chignolin'];p=c['provenance']
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyX',fontName='Helvetica',fontSize=10.5,leading=15,spaceAfter=9))
styles.add(ParagraphStyle(name='CaptionX',fontName='Helvetica',fontSize=9,leading=12,spaceAfter=10,textColor=HexColor('#334755')))
styles['Title'].textColor=HexColor('#163447');styles['Heading1'].textColor=HexColor('#163447')
story=[]
def para(t):story.append(Paragraph(t,styles['BodyX']))
def small(t):story.append(Paragraph(t,styles['CaptionX']))
def head(t):story.append(Paragraph(t,styles['Heading1']))
def fig(name,width=480):
    from PIL import Image as PI
    w,h=PI.open(SRC/name).size;story.append(Image(str(SRC/name),width=width,height=width*h/w))
def page():story.append(PageBreak())
def section(label,status,done,nextstep):
    story.append(Paragraph(label+' <font color="#167E79">['+status+']</font>',styles['Heading2']))
    para('<b>Evidence / work completed.</b> '+done)
    para('<b>Required next step.</b> '+nextstep)

story.append(Paragraph('From an illustrative atlas<br/>to a testable dynamical model',styles['Title']))
para('<b>Robustness audit and revision specification</b><br/>Joseph Campagna, PSM | October 21, 2026')
para('This report audits every limitation category in the original molecular-atlas paper. It separates measured diagnostics from proposed fixes and unresolved prerequisites. The legacy viewer and its figures remain an illustrative baseline; neither their appearance nor passing software tests validates folding dynamics.')
para(f'<b>Data analyzed:</b> 750,000 alanine frames in three runs; {c["frames"]:,} CLN025 frames in {c["runs"]:,} trajectories. '
     + ('The complete CLN025 archive was downloaded and its size and published MD5 verified.' if full else 'CLN025 results currently cover the first 128 archive members.'))
if full:
    para(f'{sum(x["frames"]<500 for x in p["timing"])} trajectories have fewer than 500 frames; the shortest has {min(x["frames"] for x in p["timing"])}. Actual lengths, not nominal duration, determine every lag pair. All raw CLN025 intervals remain 100,000 ps, so the metadata conflict persists across the full archive.')
para('<b>Decision:</b> do not promote pooled occupancy to free energy or select a compositional interface on appearance. First establish predictive sufficiency, sampling support, clock provenance and geometric validity. A meaningful non-equilibrium height can be measured without making thermodynamic claims.')
head('What is now implemented')
for text in [
    'Integrity checking and complete-archive acquisition; chemical identity, local geometry and raw timestamp inventory.',
    'Within-run transition estimation, nearest-state versus last-core comparisons, implied-timescale diagnostics, held-out Chapman-Kolmogorov comparisons and stationary-flux asymmetry diagnostics.',
    'A conditional structural-mobility height with a support mask and block/run-resampling spread; no interpolation across unsupported bins.',
    'Periodic-cover sensitivity and GF(2) topology checks including tetrahedra; mesh connectivity, boundaries, degeneracy, displacement and area checks.',
    'A training-only scaled, held-out feature prediction screen and thirteen automated invariant/asset tests.'
]:para('&#8226; '+text)
para('<b>What is not established:</b> a calibrated equilibrium estimator, validated kinetic rates, a native-state definition, independent adaptive lineages, collision-free molecular surfaces, a configuration-space nerve theorem, or semantics for composing open dynamical systems.')
page();head('1. A height with an explicit observable')
para('Let d(X) be the vector of all pairwise distances among the ten displayed sites. Define m<sub>lag</sub>(X<sub>t</sub>) as the RMS difference between d(X<sub>t+lag</sub>) and d(X<sub>t</sub>). In each occupied chart bin, estimate h = mean(m<sub>lag</sub> | X<sub>t</sub> in bin). Units are nm, not energy. Rigid rotation and translation cancel. No native structure, state assignment, or equilibrium weighting is needed for this descriptive conditional mean.')
para('The current diagnostic uses 100 frames = 100 ps for alanine and 10 frames for CLN025. These are declared exploratory lags, not selected physical timescales. CLN025 is not converted to ns. The two systems use different site selections and are not quantitatively compared.')
para('This remains a conditional mean for the sampled ensemble. Adaptive initialization can change the mixture of hidden conformations within a chart bin, and therefore change this height. Giving the height physical length units does not remove sampling bias or prove a sufficient state representation.')
fig('mobility-height.png')
para('A bin is displayed only with at least 100 retained lag pairs, five contributing blocks, and three contributing runs; CLN025 additionally requires three inferred ancestral roots. CLN025 resamples entire inferred roots, while alanine resamples within-run blocks. These are reporting thresholds, not proof of convergence. The 200-replicate interval is conditional spread, not a calibrated confidence interval: alanine has only three runs and root independence is unverified. Block-length, lag and bin-size sensitivity remain required.')
page();head('The same overlap relations, a different vertical observable')
fig('mobility-nerve.png')
para('This prototype keeps the legacy CLN025 overlap category fixed and replaces the vertical encoding with the measured conditional structural displacement. It demonstrates how the scientific meaning and appearance of the landscape change together. It is not a new cover fitted to the complete deposit, and it is not a free-energy manifold.')
para('The figure displays only vertices with supported heights and the faces whose vertices all have supported heights. Vertical bars show conditional resampling spread. Missing heights are stored as null in the exported JSON, never as zero. The JSON retains all original nodes, edges and faces so that a visualization mask cannot silently change the underlying categorical data.')
para('A production landscape should add molecular relief as a separately scaled visual layer, retain the numeric observable at each anchor, and show uncertainty and unsupported regions explicitly. Changing the height does not authorize equilibrium or kinetic interpretations that the estimator cannot support.')
page();head('2. Dynamics: diagnose before interpreting')
fig('kinetic-diagnostics.png')
for name,s in [('Alanine',a),('CLN025',c)]:
    models=s['legacy_core_models'];first=models[0];last=models[-1]
    tau0=first.get('implied_times_frames',[float('nan')])[0];tau1=last.get('implied_times_frames',[float('nan')])[0]
    para(f'<b>{name}.</b> With legacy last-core labels the slowest positive-real implied timescale changes from {tau0:.1f} frames at lag {first["lag_frames"]} to {tau1:.1f} frames at lag {last["lag_frames"]}. This must be read together with nearest-center results and held-out error, not as an automatically validated relaxation time.')
para('The CK panel compares P(lag)<sup>k</sup> learned on training runs with direct counts at k*lag on held-out runs, for k=2,4. Each point is the maximum over folds and multiples of the row-count-weighted total-variation discrepancy. Small weighted errors can conceal a poorly predicted rare state; the JSON includes every row, prediction and observation. These are diagnostics, not formal pass/fail significance tests.')
para('Alanine folds leave out a complete trajectory. CLN025 folds keep all descendants of a filename-inferred ancestral root together; an epoch-only split is retained as sensitivity data. Legacy state centers are held fixed, not newly optimized on the holdout. State definitions originally used the prototype data, so this is not a clean independent model-selection benchmark. Inferred roots are not necessarily independent preparations. Last-core labels encode history and must not be mistaken for an instantaneous state partition.')
if 'lineage' in p:
    lineage=p['lineage']
    para(f'The inferred genealogy has {lineage["inferred_roots"]} roots; the largest contains {lineage["largest_root_runs"]:,} trajectories. Fold run counts are {lineage["fold_run_counts"]}. This imbalance must be retained in interpretation rather than hidden by a random trajectory split.')
page();head('3. Topology and geometry: retain the missing information')
fig('topology-sensitivity.png')
para('This sensitivity experiment constructs 18 periodic farthest-point cover centers and holds them fixed while varying the metric, radius and witness stride. It is a new audit cover, not a recalculation of the old viewer with unchanged centers. Betti numbers refer only to the sampled witnessed complex. Tetrahedral boundaries can fill apparent cavities created by truncating at triangles; higher-dimensional faces cannot be discarded when making homology claims.')
para('A periodic metric addresses the alanine angular seam in distance calculations. It does not by itself establish a good cover, sample completeness or a theorem about the underlying configuration space. A future renderer should show seam-equivalent vertices consistently, retain higher-simplex metadata and distinguish the displayed 2-skeleton from the analyzed complex.')
for name,s in [('Alanine',a),('CLN025',c)]:
    rows=s['mesh']['routes'];n=sum(x['components']>1 for x in rows)
    para(f'<b>{name} mesh audit:</b> {n} of {len(rows)} route skins have multiple connected components; the maximum component count is {max(x["components"] for x in rows)}. This identifies a rendering/data construction issue to inspect, not a new molecular state.')
para('Combinatorial checks do not establish absence of self-intersection or collisions. Swept skins should remain labeled as explanatory envelopes. A scientifically timed animation should use recorded conformers, or interpolation explicitly constrained and checked against molecular geometry. A visually pleasing displacement field is not a molecular dynamical law.')
page();head('4. Limitation register: data and inference')
section('Dataset scale and selection','narrowly resolved' if full else 'open',
        f'{c["runs"]:,} trajectories and {c["frames"]:,} frames analyzed. '+('Archive size and MD5 match the deposit; member hashes are checked during parsing.' if full else 'The legacy 128-run subset is audited.'),
        'Preserve both the original subset and full-deposit results. Full coverage of the deposit does not remove adaptive initialization bias or missing conformational regions.')
section('Timing conflict','unresolved',
        'Raw first/last times and intervals are preserved per trajectory. Frame-index calculations do not silently multiply or divide time by 1,000.',
        'Recover the simulation output stride or obtain depositor confirmation before reporting physical rates or times for CLN025. Do not use an inferred correction as established metadata.')
section('Adaptive sampling and comparability','quantified, not corrected',
    'Conditional transitions, held-out inferred-lineage checks and resampling spread replace reliance on pooled density alone. Stationary distributions and flux asymmetry are exported as diagnostics, not equilibrium estimates.',
        'Validate adaptive genealogy; compare appropriate nonstationary estimators and state discretizations. Calibrate uncertainty by lineage/epoch and independent trajectories. Do not force detailed balance to make plots appear thermodynamic.')
section('Chemical identity and cartoons','partly checked',
        'CA identity and CLN025 sequence are checked; backbone phi/psi features are extracted from N/CA/C coordinates. Neighbor-distance ranges are retained for every run.',
        'Establish an explicit topology/capping mapping, PBC treatment, native reference and atom/element assignments before hydrogen-bond, contact-native or secondary-structure claims. CA compactness remains geometric, not mass-weighted.')
outlier=SRC/'geometry-outlier.json'
if full and outlier.exists():
    g=json.loads(outlier.read_text())
    para(f'<b>A chemistry-sensitive exception.</b> {g["file"]}, frame {g["frame"]}, has a minimum CA spacing of {g["CA_distance_nm"]:.4f} nm at Asp3-Pro4 and peptide omega {g["omega_degrees"]:.2f} degrees. This is consistent with a cis peptide and exposes the inadequacy of the old blanket 0.3 nm cutoff. The raw frame is retained; a geometry audit should inspect bond geometry and omega rather than automatically discard it. The current feature screen includes phi/psi, not omega; omega should be tested explicitly in a follow-up.')
page();head('5. Limitation register: models and semantics')
section('Projection and state definitions','falsification in progress',
        'Nearest-state and last-core models are evaluated separately. A held-out ridge screen compares geometric coordinates, CA distances, periodic backbone torsions and their combination.',
        'Use nested, lineage-aware validation for feature/state/lag selection; test memory and metastability. Evaluate more flexible models against persistence baselines. Contact cutoffs, state counts, smoothing and bin scales need systematic sensitivity.')
section('Categorical claims','scope corrected; theorem unresolved',
        'Periodic-distance and higher-face topology diagnostics expose consequences of the cut chart and truncation. Exact inclusion composition remains a combinatorial statement.',
        'Store maximal simplices, verify closure, preserve periodic identifications and report stable features across cover scales. Define any comparison functor and prove its laws before identifying overlap and path categories. Do not claim configuration-space homotopy recovery.')
section('Statistical and dynamical validation','diagnostics implemented',
        'Within-run lag counts, implied timescales, held-out CK discrepancy and flux asymmetry are computed. Counts never cross trajectory boundaries; unsupported rows remain missing rather than becoming absorbing states.',
        'Add calibrated correlated-data uncertainty, rare-state error criteria, lag/state sensitivity and independent experimental or simulation checks. No rate, barrier, committor or equilibrium population is approved by this audit.')
section('Composition of dynamical systems','research requirement',
        'Formal composable words remain distinct from consecutive recorded passages. Last-core history is explicitly identified.',
        'Specify state spaces, boundary variables, admissible couplings and behavior semantics. Demonstrate predictive agreement for composed versus jointly simulated models before claiming a compositional dynamics framework.')
page();head('6. Limitation register: surfaces and delivery')
section('Deformation and geometry','audited, not physically repaired',
        'Route meshes are checked for components, boundary/nonmanifold edges, degenerate triangles, bounded displacement and area variation at stored keyframes.',
        'Check self-intersections throughout interpolation; compare recorded-frame and constrained-coordinate representations. Keep illustrative skins separate from physical conformations. A Boolean union cannot repair statistical or molecular validity.')
section('Rendering and software constraints','partly mitigated',
        'The audit is offline and independent of Blender/browser rendering. Thirteen tests cover run boundaries, missing support, rigid-motion invariance, synthetic Markov dynamics, inferred lineage splits, tetrahedral topology and existing assets.',
        'Pin an audit environment, add browser/GPU regression tests and coordinate-aware normals. Re-render molecular relief only after the chosen field has units, uncertainty and support masks. Preserve raw timestamps and metadata in every export.')
section('Publication and reproducibility','local revision',
        'Source scripts and machine-readable results reproduce this audit; original viewer assets are retained. No external messages are sent and no audit publication is performed in this pass.',
        'Resolve CI credentials through the account owner when publication is desired. Publish a versioned validation dataset, figure provenance, environment lock and limitations table together, not isolated improved-looking figures.')
head('Acceptance gates before interface selection')
para('1. Verified data identity, lineage, clock and independent split.<br/>2. Predictive sufficiency against persistence and simpler models.<br/>3. Lag/state stability and CK error within justified uncertainty, including rare states.<br/>4. Supported height field with units and calibrated uncertainty.<br/>5. Stable nerve construction and honest geometric representation.<br/>6. Explicit interface and composition laws, tested against coupled dynamics.')
page();head('7. Interface hypotheses and figure revision')
para('<b>Hypothesis only:</b> periodic torsions are a natural baseline for alanine; for CLN025, nonlocal distances or contacts together with periodic backbone torsions may expose states merged by (Rg, end-to-end distance). Feature predictability is necessary evidence, not proof that an observable is a valid compositional interface. Solvent, velocities and unresolved memory may require additional variables or a stochastic/history-dependent model.')
screen=SRC/('full-feature-screen.json' if full else 'subset-feature-screen.json')
if screen.exists():
    z=json.loads(screen.read_text());results=z['results']
    para('The initial feature screen uses a fixed linear ridge model to predict future CA distance vectors, with training-only scaling and held-out inferred-root groups. A ratio below one means lower squared error than persistence; it is not a universal model score.')
    table=[['Features','Lag 10: median MSE / persistence']]
    import statistics
    for name in ['Rg_end_to_end','all_CA_distances','backbone_sin_cos','distances_plus_torsions']:
        vals=[x['mse_ratio_to_persistence'] for x in results if x['features']==name and x['lag_frames']==10]
        table.append([name.replace('_',' '),f'{statistics.median(vals):.3f}'])
    t=Table(table,colWidths=[220,265]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#E8F0F2')),('FONTSIZE',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]));story.append(t);story.append(Spacer(1,12))
    para('The prediction target is itself a CA-distance vector, which favors distance-based inputs. This screen cannot establish a universally best representation or a compositional interface; additional target observables, nonlinear models and independent evaluation are required.')
para('<b>Figures should change substantively.</b> Replace unqualified occupancy-height landscapes with a declared observable plus uncertainty and missing-support regions. Show kinetics panels next to route geometry; distinguish a visual phase from simulation time. Preserve the full nerve data even when only its 2-skeleton is drawn. The former deformation triptychs (including the old paper\'s Figure 9) should be labeled illustrative or paired with recorded-conformation geometry checks, not recaptioned as validated trajectories.')
para('<b>Future thermodynamic height:</b> -kBT log(pi) is appropriate only after validating the equilibrium estimator and coarse-graining convention. <b>Future reactive height:</b> a committor or mean first-passage time requires defined A/B sets and validated kinetics. Neither is currently justified by the existing four-state CLN025 model.')
head('Reproduction and primary references')
small('From alanine-nerve/:<br/><font face="Courier" size="9">python verify_full_chignolin.py<br/>python robustness.py --full<br/>python feature_screen.py --full<br/>python inspect_geometry_outlier.py<br/>python plot_robustness.py<br/>python -m unittest discover -s tests -v<br/>python build_robustness_report.py</font>')
small('Data: <link href="https://doi.org/10.6084/m9.figshare.13858898" color="blue">Perez Culubret and De Fabritiis, Chignolin Simulations, CC BY 4.0</link>.<br/>Adaptive-estimation cautions: <link href="https://doi.org/10.1063/1.5142457" color="blue">Wan and Voelz (2020), Adaptive Markov state model estimation using short reseeding trajectories</link>.<br/>Model selection: <link href="https://arxiv.org/abs/1407.8083" color="blue">McGibbon and Pande, Variational cross-validation of slow dynamical modes</link>.<br/>Nonstationary estimation: <link href="https://arxiv.org/abs/1701.01665" color="blue">Nuske et al., Markov State Models from short non-Equilibrium Simulations</link>.')
def footer(canvas,doc):
    canvas.setFont('Helvetica',8);canvas.setFillColor(HexColor('#334755'))
    canvas.drawString(48,25,'Joseph Campagna, PSM | Robustness audit | Exploratory; not peer reviewed')
    canvas.drawRightString(564,25,str(doc.page))
target=OUT/'molecular-atlas-robustness-audit.pdf'
doc=SimpleDocTemplate(str(target),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=42,bottomMargin=46,
                      title='Molecular Atlas: Robustness Audit',author='Joseph Campagna, PSM')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(target)
