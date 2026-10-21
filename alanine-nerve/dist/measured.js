import * as THREE from 'three';
import {OrbitControls} from './OrbitControls.js';
const $=id=>document.getElementById(id);
const renderer=new THREE.WebGLRenderer({canvas:$('scene'),antialias:true,preserveDrawingBuffer:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setClearColor(0x080e19);
const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(42,1,.1,200),world=new THREE.Group();scene.add(world);
const controls=new OrbitControls(camera,$('scene'));controls.enableDamping=true;
scene.add(new THREE.HemisphereLight(0xe2f5ff,0x152331,2.4));
const key=new THREE.DirectionalLight(0xffffff,3);key.position.set(-12,26,10);scene.add(key);
const miniRenderer=new THREE.WebGLRenderer({canvas:$('mini'),antialias:true});miniRenderer.setClearColor(0x101c2b);miniRenderer.setPixelRatio(Math.min(devicePixelRatio,2));
const miniScene=new THREE.Scene(),miniCamera=new THREE.PerspectiveCamera(38,1,.01,50);miniScene.add(new THREE.HemisphereLight(0xffffff,0x203040,3));miniCamera.position.set(0,0,5);
let data,recorded,nerveGroup,plateGroup,reliefGroup,intervalGroup,tiles=[],miniObject=null,marker=null,playing=false,lastFrame=0,request=0,scale=1;
const ray=new THREE.Raycaster(),pointer=new THREE.Vector2();
function dispose(group){group.traverse(o=>{o.geometry?.dispose();for(const m of [].concat(o.material||[])){m.map?.dispose();m.dispose();}});group.clear();}
function line(points,color,opacity=.7){const g=new THREE.BufferGeometry().setFromPoints(points);return new THREE.Line(g,new THREE.LineBasicMaterial({color,transparent:true,opacity}));}
function map(q,h,lift=0){
 if($('torus').checked&&data.system==='alanine'){
  const a=q[0]*Math.PI/180,b=q[1]*Math.PI/180,r=4+h*scale*.25+lift*.25;
  return new THREE.Vector3((10+r*Math.cos(b))*Math.cos(a),r*Math.sin(b)+5,(10+r*Math.cos(b))*Math.sin(a));
 }
 const [lo,hi]=data.height.limits;return new THREE.Vector3((q[0]-lo[0])/(hi[0]-lo[0])*30-15,h*scale+lift,(q[1]-lo[1])/(hi[1]-lo[1])*30-15);
}
function color(v,max){return new THREE.Color().setHSL(.47-.39*Math.min(1,Math.max(0,v/(max||1))),.65,.53);}
function sites(coords,bonds,size=.04){
 const g=new THREE.Group();
 coords.forEach((p,i)=>{const s=new THREE.Mesh(new THREE.SphereGeometry(size,8,6),new THREE.MeshStandardMaterial({color:new THREE.Color().setHSL(.58-.48*i/(coords.length-1),.6,.64),roughness:.45}));s.position.set(...p);g.add(s);});
 bonds.forEach(([a,b])=>g.add(line([new THREE.Vector3(...coords[a]),new THREE.Vector3(...coords[b])],0x9acacb,1)));
 return g;
}
function showMolecule(coords){
 if(miniObject){dispose(miniObject);miniScene.remove(miniObject);}
 miniObject=sites(coords,recorded.bonds);miniScene.add(miniObject);
 const extent=Math.max(...coords.map(p=>Math.hypot(...p)));miniCamera.position.z=Math.max(2,extent*3.8);miniCamera.lookAt(0,0,0);
}
function reset(){
 if(!data){camera.position.set(37,32,-42);controls.target.set(0,5,0);return;}
 const box=new THREE.Box3().setFromObject(world);if(box.isEmpty()){camera.position.set(37,32,-42);controls.target.set(0,5,0);return;}
 const center=box.getCenter(new THREE.Vector3()),dir=new THREE.Vector3(1,.85,-1.1).normalize();
 camera.position.copy(center.clone().add(dir));camera.lookAt(center);const inv=camera.quaternion.clone().invert();
 const pts=[];for(const x of [box.min.x,box.max.x])for(const y of [box.min.y,box.max.y])for(const z of [box.min.z,box.max.z])pts.push(new THREE.Vector3(x,y,z).sub(center).applyQuaternion(inv));
 const tangent=Math.tan(camera.fov*Math.PI/360),distance=Math.max(...pts.map(p=>Math.max(Math.abs(p.y)/tangent,Math.abs(p.x)/(tangent*camera.aspect))+p.z))*1.2;
 camera.position.copy(center.clone().addScaledVector(dir,distance));controls.target.copy(center);controls.update();
}
function build(){
 dispose(world);tiles=[];nerveGroup=new THREE.Group();plateGroup=new THREE.Group();reliefGroup=new THREE.Group();intervalGroup=new THREE.Group();world.add(nerveGroup,plateGroup,reliefGroup,intervalGroup);
 const h=data.height,n=h.bins,[lo,hi]=h.limits,values=h.height_nm.flat().filter((v,k)=>Number.isFinite(v)&&h.supported[Math.floor(k/n)][k%n]);scale=10/(Math.max(...values)||1);
 const mode=$('color').value;
 const value=(i,j)=>mode==='height'?h.height_nm[i][j]:mode==='spread'?h.conditional_resampling_interval_nm[1][i][j]-h.conditional_resampling_interval_nm[0][i][j]:h.raw_largest_unit_fraction[i][j];
 let max=0;for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(h.supported[i][j])max=Math.max(max,value(i,j));
 for(let i=0;i<n;i++)for(let j=0;j<n;j++){
  if(!h.supported[i][j])continue;
  const q=(a,b)=>[lo[0]+(i+a)/n*(hi[0]-lo[0]),lo[1]+(j+b)/n*(hi[1]-lo[1])],y=h.height_nm[i][j];
  const p=[[0,0],[1,0],[1,1],[0,1]].map(([a,b])=>map(q(a,b),y));
  const geo=new THREE.BufferGeometry().setFromPoints(p);geo.setIndex([0,2,1,0,3,2]);geo.computeVertexNormals();
  const mesh=new THREE.Mesh(geo,new THREE.MeshBasicMaterial({color:color(value(i,j),max),side:THREE.DoubleSide}));mesh.userData={i,j};world.add(mesh);tiles.push(mesh);
  world.add(line([...p,p[0]],0x223c48,.7));
  intervalGroup.add(line([map(q(.5,.5),h.conditional_resampling_interval_nm[0][i][j]),map(q(.5,.5),h.conditional_resampling_interval_nm[1][i][j])],0xf5efff,.6));
 }
 const nodes=data.cover.nodes,positions=nodes.map(n=>n.supported?map(n.chart,n.height_nm,2):null);
 function seam(ids){return data.system==='alanine'&&!$('torus').checked&&[0,1].some(axis=>Math.max(...ids.map(i=>nodes[i].chart[axis]))-Math.min(...ids.map(i=>nodes[i].chart[axis]))>180);}
 let hiddenSeams=0;
 for(const [a,b] of data.cover.edges){
  if(!positions[a]||!positions[b])continue;
  if(seam([a,b])){hiddenSeams++;continue;}
  if($('torus').checked&&data.system==='alanine'){
   const qa=nodes[a].chart,qb=nodes[b].chart,delta=qb.map((v,j)=>((v-qa[j]+540)%360)-180);
   const pts=Array.from({length:17},(_,k)=>map(qa.map((v,j)=>v+delta[j]*k/16),nodes[a].height_nm*(1-k/16)+nodes[b].height_nm*k/16,2));nerveGroup.add(line(pts,0xd5ecf4,.45));
  }else nerveGroup.add(line([positions[a],positions[b]],0xd5ecf4,.45));
 }
 for(const ids of data.cover.chains){
  if(ids.some(i=>!positions[i])||seam(ids))continue;
  const geo=new THREE.BufferGeometry().setFromPoints(ids.map(i=>positions[i]));geo.computeVertexNormals();plateGroup.add(new THREE.Mesh(geo,new THREE.MeshBasicMaterial({color:0xafcede,transparent:true,opacity:.055,depthWrite:false,side:THREE.DoubleSide})));
 }
 nodes.forEach((n,i)=>{if(!positions[i])return;const m=new THREE.Mesh(new THREE.IcosahedronGeometry(.12,1),new THREE.MeshBasicMaterial({color:[0x8af1c3,0x78b7ef,0xffcc83][n.simplex.length-1]}));m.position.copy(positions[i]);nerveGroup.add(m);});
 for(const a of recorded.anchors){const [i,j]=a.bin;if(!h.supported[i][j])continue;const mol=sites(a.coords_nm,recorded.bonds,.025);mol.scale.setScalar(data.system==='alanine'?1.4:.65);mol.position.copy(map(a.chart,h.height_nm[i][j],.35));reliefGroup.add(mol);}
 nerveGroup.visible=$('nerve').checked;plateGroup.visible=$('nerve').checked&&$('plates').checked;reliefGroup.visible=$('relief').checked;intervalGroup.visible=$('intervals').checked;
 $('legend').textContent=mode==='height'?'MEAN STRUCTURAL MOBILITY':mode==='spread'?'CONDITIONAL RESAMPLING WIDTH':'LARGEST UNIT CONTRIBUTION';
 $('range').textContent=`0 → ${max.toFixed(3)} ${mode==='dominance'?'fraction':'nm'} · height always mobility`;
 document.querySelector('.gradient').style.background=`linear-gradient(to right,${Array.from({length:11},(_,i)=>color(i/10,1).getStyle()).join(',')})`;
 $('axes').textContent=$('torus').checked?'Torus angles: φ, ψ; radial relief encodes mobility.':'Horizontal/depth: '+(data.system==='alanine'?'φ / ψ (degrees)':'Cα Rg / end-to-end distance (nm)')+'; height: mobility (nm)';
 $('nerveInfo').textContent=`${nodes.length} display objects; ${data.cover.edges.length} inclusions; ${data.cover.chains.length} triangles. Full base complex dimension ${data.cover.max_dimension}. ${nodes.filter(n=>!n.supported).length} unsupported vertices hidden. ${hiddenSeams} seam-crossing edges hidden in cut view; use torus view.`;
 marker=null;showFrame();
}
function showFrame(){
 if(!data||!recorded)return;
 const path=recorded.excerpts[+$('excerpt').value||0],index=Math.min(+$('frame').value,path.frames.length-1),f=path.frames[index];$('frame').max=path.frames.length-1;showMolecule(f.coords_nm);
 if(marker){dispose(marker);world.remove(marker);}
 marker=sites(f.coords_nm,recorded.bonds,.04);marker.scale.setScalar(2);
 const h=data.height,[lo,hi]=h.limits,ij=f.chart.map((v,k)=>Math.floor((v-lo[k])/(hi[k]-lo[k])*h.bins));const valid=ij.every(v=>v>=0&&v<h.bins)&&h.supported[ij[0]][ij[1]];
 if(valid){marker.position.copy(map(f.chart,h.height_nm[ij[0]][ij[1]],1));world.add(marker);}
 $('frameInfo').textContent=`Run ${path.run}, recorded frame ${f.frame}${recorded.physical_frame_interval_ps===null?' · physical clock unresolved':` · ${f.frame} ps`}. ${valid?'Placed at supported mobility height.':'Unsupported height: main-scene marker omitted; recorded geometry remains in inset.'}`;
 window.atlasState={system:data.system,tiles:tiles.length,frame:f.frame,run:path.run,physicalClock:recorded.physical_frame_interval_ps,finite:tiles.every(o=>Array.from(o.geometry.attributes.position.array).every(Number.isFinite))};
}
async function load(){
 const token=++request;playing=false;$('play').textContent='Play recorded frames';$('loading').hidden=false;const name=$('system').value;
 const get=async path=>{const r=await fetch(path);if(!r.ok)throw Error(`${r.status}: ${path}`);return r.json();};
 const [a,b]=await Promise.all([get(`./validation/${name}-atlas.json`),get(`./validation/${name}-recorded.json`)]);if(token!==request)return;data=a;recorded=b;
 $('torus').checked=false;$('torus').disabled=name!=='alanine';$('frame').value=0;
 $('excerpt').replaceChildren(...b.excerpts.map((p,i)=>{const o=document.createElement('option');o.value=i;o.textContent=`Run ${p.run}: frames ${p.frames[0].frame}–${p.frames.at(-1).frame}`;return o;}));
 $('title').textContent=name==='alanine'?'Alanine dipeptide':'Chignolin variant CLN025';$('subtitle').textContent=`${a.frames.toLocaleString()} frames · ${a.runs.toLocaleString()} trajectories · ${a.clock}`;
 $('summary').textContent=`Lag ${a.height.lag_frames} frames${name==='alanine'?` = ${a.height.lag_frames} ps`:''}; RMS change over 45 pair distances among ten ${name==='alanine'?'heavy atoms':'Cα sites'}. ${a.height.estimand} Site selections and averaging differ between systems; do not compare heights as thermodynamic quantities.`;
 $('download').href=`./validation/${name}-atlas.json`;build();reset();$('loading').hidden=true;
}
$('system').onchange=()=>load().catch(error);$('color').onchange=build;$('torus').onchange=()=>{build();reset();};
$('nerve').onchange=()=>{nerveGroup.visible=$('nerve').checked;plateGroup.visible=$('nerve').checked&&$('plates').checked;};$('plates').onchange=()=>plateGroup.visible=$('nerve').checked&&$('plates').checked;
$('relief').onchange=()=>reliefGroup.visible=$('relief').checked;$('intervals').onchange=()=>intervalGroup.visible=$('intervals').checked;
$('frame').oninput=()=>{playing=false;$('play').textContent='Play recorded frames';showFrame();};$('excerpt').onchange=()=>{$('frame').value=0;showFrame();};
$('play').onclick=()=>{playing=!playing;$('play').textContent=playing?'Pause recorded frames':'Play recorded frames';};$('reset').onclick=reset;$('top').onclick=()=>{camera.position.set(0,65,.01);controls.target.set(0,4,0);};
$('capture').onclick=()=>{renderer.render(scene,camera);const a=document.createElement('a');a.href=$('scene').toDataURL();a.download=`${data.system}-measured.png`;a.click();};
$('scene').addEventListener('click',e=>{if(!data)return;const r=$('scene').getBoundingClientRect();pointer.set((e.clientX-r.left)/r.width*2-1,-(e.clientY-r.top)/r.height*2+1);ray.setFromCamera(pointer,camera);const hit=ray.intersectObjects(tiles)[0];if(!hit)return;const {i,j}=hit.object.userData,h=data.height,a=recorded.anchors.find(a=>a.bin[0]===i&&a.bin[1]===j);if(a){playing=false;$('play').textContent='Play recorded frames';showMolecule(a.coords_nm);}
 $('inspector').textContent=`Bin (${i}, ${j})\nMean mobility ${h.height_nm[i][j].toFixed(5)} nm\nConditional spread ${h.conditional_resampling_interval_nm.map(v=>v[i][j].toFixed(5)).join(' – ')} nm\n${h.count[i][j]} lag pairs; ${h.run_support[i][j]} runs\nEffective resampling-unit contributions ${h.effective_resampling_units[i][j].toFixed(2)}\nLargest contribution ${(100*h.largest_unit_fraction[i][j]).toFixed(1)}%\n${a?`Representative: run ${a.run}, frame ${a.frame}`:''}`;
});
function resize(){for(const [r,c,el] of [[renderer,camera,$('scene')],[miniRenderer,miniCamera,$('mini')]]){const b=el.getBoundingClientRect();r.setSize(b.width,b.height,false);c.aspect=b.width/b.height;c.updateProjectionMatrix();}}
new ResizeObserver(resize).observe($('scene'));resize();reset();
function animate(t){requestAnimationFrame(animate);if(playing&&t-lastFrame>125){const next=+$('frame').value+1;if(next>+$('frame').max){playing=false;$('play').textContent='Play recorded frames';}else{$('frame').value=next;showFrame();}lastFrame=t;}controls.update();renderer.render(scene,camera);miniRenderer.render(miniScene,miniCamera);}requestAnimationFrame(animate);
function error(e){$('loading').hidden=false;$('loading').textContent='Unable to load measurement data: '+e.message;console.error(e);}
load().catch(error);
