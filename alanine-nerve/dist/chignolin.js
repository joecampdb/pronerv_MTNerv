import * as THREE from 'three';
import {OrbitControls} from './OrbitControls.js';
import {loadPathSkins} from './path-skins.js';
import {backboneCartoon,disposeGroup} from './cartoon.js';
const $=id=>document.getElementById(id), canvas=$('scene');
const renderer=new THREE.WebGLRenderer({canvas,antialias:true,preserveDrawingBuffer:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setClearColor(0x080e19,0);
const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(42,1,.1,200);
camera.position.set(38,33,-43);
const controls=new OrbitControls(camera,canvas);controls.target.set(0,3,0);controls.enableDamping=true;
scene.add(new THREE.HemisphereLight(0xd5ffff,0x172032,2.4));
for(const [p,c] of [[[20,30,10],0xd5ffff],[[-20,15,-20],0xffb89a]]){
 const l=new THREE.DirectionalLight(c,3);l.position.set(...p);scene.add(l);
}
const world=new THREE.Group(),nerve=new THREE.Group(),dynamic=new THREE.Group();
scene.add(world);world.add(nerve,dynamic);
const grid=new THREE.GridHelper(30,6,0x2b4657,0x182d3e);grid.position.y=-3;scene.add(grid);
const palette=['#4cf1bc','#38b6d9','#7377da','#df8aaa','#ffce83'].map(c=>new THREE.Color(c));
const basinColors=[0x69e8b4,0xffc277,0xaf90ff,0xf38eaa];
function color(e){const f=Math.max(0,Math.min(3.999,e/8*4)),i=Math.floor(f);return palette[i].clone().lerp(palette[i+1],f-i);}
let data,skins=[],terrain,phase=0,paused=false,previous=0,selected=-1,pair=null;
const miniRenderer=new THREE.WebGLRenderer({canvas:$('mini'),antialias:true});
miniRenderer.setPixelRatio(Math.min(devicePixelRatio,2));miniRenderer.setClearColor(0x101c2b);
const miniScene=new THREE.Scene(),miniCamera=new THREE.PerspectiveCamera(38,1,.01,100),mol=new THREE.Group();
miniCamera.position.set(0,0,5);miniScene.add(mol,new THREE.HemisphereLight(0xffffff,0x172032,3));
const ml=new THREE.DirectionalLight(0xffffff,3);ml.position.set(3,4,5);miniScene.add(ml);
function showCartoon(coords){disposeGroup(mol);mol.add(backboneCartoon(coords));}
function line(points,c,opacity=.5){const g=new THREE.BufferGeometry().setFromPoints(points);
 return new THREE.Line(g,new THREE.LineBasicMaterial({color:c,transparent:true,opacity}));}
function routeFilter(){
 skins.forEach((s,i)=>s.mesh.visible=$('pathSkins').checked&&(pair?pair.includes(i):selected<0||i===selected));
 $('details').textContent=pair?'Formal composition of independently observed route types; not a spliced trajectory.':
 selected<0?'All route types. The inset shows a compact representative Cα trace.':
 `Run ${data.routes[selected].run+1}, frames ${data.routes[selected].startFrame}–${data.routes[selected].endFrame}; ${data.routes[selected].count} observed passages.`;
}
function compose(){
 disposeGroup(dynamic);pair=$('pathChain').value?$('pathChain').value.split(',').map(Number):null;
 if(pair){
  const a=data.routes[pair[0]],b=data.routes[pair[1]];
  const p=[a.source,a.target,b.target].map(i=>new THREE.Vector3(...data.basins[i].pos).add(new THREE.Vector3(0,3,0)));
  if(a.source===b.target)p[2].add(new THREE.Vector3(2,2,0)); // formal repeated object, separated for legibility
  dynamic.add(line([p[0],p[1],p[2]],0xffdc94,1));
  const geo=new THREE.BufferGeometry().setFromPoints([p[0],p[2]]),mat=new THREE.LineDashedMaterial({color:0xffdc94,dashSize:.5,gapSize:.3});
  const l=new THREE.Line(geo,mat);l.computeLineDistances();dynamic.add(l);
  const face=new THREE.BufferGeometry().setFromPoints(p);face.computeVertexNormals();
  dynamic.add(new THREE.Mesh(face,new THREE.MeshBasicMaterial({color:0xffdc94,transparent:true,opacity:.18,side:THREE.DoubleSide,depthWrite:false})));
  $('composition').textContent=`${data.basins[a.source].name} → ${data.basins[a.target].name} → ${data.basins[b.target].name}. Dashed edge: g ∘ f; not a direct observed generator.`;
 }else $('composition').textContent='Select two composable generators to superimpose a path-nerve 2-simplex.';
 routeFilter();
}
async function init(){
 const get=async f=>{const r=await fetch('./chignolin/'+f);if(!r.ok)throw Error(`${f}: ${r.status}`);return r;};
 const [d,vb,ib]=await Promise.all([get('data.json').then(r=>r.json()),get('surface.bin').then(r=>r.arrayBuffer()),get('triangles.bin').then(r=>r.arrayBuffer())]);
 data=d;const raw=new Float32Array(vb),p=[],n=[],c=[];
 for(let i=0;i<raw.length;i+=7){p.push(...raw.subarray(i,i+3));n.push(...raw.subarray(i+3,i+6));c.push(...color(raw[i+6]).toArray());}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.Float32BufferAttribute(p,3));g.setAttribute('normal',new THREE.Float32BufferAttribute(n,3));g.setAttribute('color',new THREE.Float32BufferAttribute(c,3));g.setIndex(new THREE.BufferAttribute(new Uint32Array(ib),1));
 terrain=new THREE.Mesh(g,new THREE.MeshStandardMaterial({vertexColors:true,transparent:true,opacity:.55,depthWrite:false,side:THREE.DoubleSide,roughness:.4}));world.add(terrain);
 const positions=d.nodes.map(n=>new THREE.Vector3(...n.pos).add(new THREE.Vector3(0,2.1,0)));
 for(const [i,j] of d.edges)nerve.add(line([positions[i],positions[j]],0xc8e9ee,.4));
 const tri=d.chains.flatMap(chain=>chain.flatMap(i=>positions[i].toArray()));
 const faces=new THREE.BufferGeometry();faces.setAttribute('position',new THREE.Float32BufferAttribute(tri,3));
 nerve.add(new THREE.Mesh(faces,new THREE.MeshBasicMaterial({color:0xa1cddd,transparent:true,opacity:.06,side:THREE.DoubleSide,depthWrite:false})));
 d.nodes.forEach((n,i)=>{const m=new THREE.Mesh(new THREE.IcosahedronGeometry(.16,1),new THREE.MeshBasicMaterial({color:[0xa8ffdb,0x81bfff,0xffd29a][n.simplex.length-1]}));m.position.copy(positions[i]);nerve.add(m);
 const o=document.createElement('option');o.value=i;o.textContent=`{${n.simplex.map(j=>'U'+j).join(', ')}} · ${n.count} witnesses`;$('nodeSelect').append(o);});
 skins=await loadPathSkins(world,d.routes.map(r=>basinColors[r.source]),'./chignolin/skins/');
 for(const r of d.routes){const o=document.createElement('option');o.value=r.id;o.textContent=`${d.basins[r.source].name} → ${d.basins[r.target].name} · ${r.count} passages`;$('route').append(o);}
 for(const pair of d.pairs){const a=d.routes[pair[0]],b=d.routes[pair[1]],o=document.createElement('option');o.value=pair.join(',');o.textContent=`${d.basins[a.source].name} → ${d.basins[a.target].name} → ${d.basins[b.target].name}`;$('pathChain').append(o);}
 $('stats').textContent=`Legacy subset: ${d.frames.toLocaleString()} frames · ${d.runs} adaptive trajectories · ${d.totalPassages.toLocaleString()} passages`;
 $('nerveStats').textContent=`${d.nodes.length} objects · ${d.edges.length} inclusions · ${d.chains.length} 2-simplices`;
 $('bounds').textContent=`Rg: ${d.chart.min[0].toFixed(2)}–${d.chart.max[0].toFixed(2)} nm; end-to-end: ${d.chart.min[1].toFixed(2)}–${d.chart.max[1].toFixed(2)} nm`;
 $('basins').textContent=d.basins.map(b=>`${b.name}: Rg ${b.features[0].toFixed(2)} nm, end-to-end ${b.features[1].toFixed(2)} nm`).join(' · ');
 showCartoon(d.cartoons[0].molecule);routeFilter();$('loading').remove();
}
$('route').onchange=e=>{selected=+e.target.value;pair=null;$('pathChain').value='';compose();update();};
$('pathChain').onchange=compose;
$('nodeSelect').onchange=e=>{const n=data.nodes[+e.target.value];paused=true;$('pause').textContent='▶ Play';showCartoon(n.molecule);$('details').textContent=`Overlap object: ${n.count} sampled witnesses; recorded global frame ${n.frame}.`;};
$('cartoonChoice').onchange=e=>{paused=true;$('pause').textContent='▶ Play';const c=data.cartoons[+e.target.value];showCartoon(c.molecule);$('details').textContent=`Recorded run ${c.run+1}, frame ${c.localFrame}; Rg ${c.features[0].toFixed(2)} nm.`;};
$('nerve').onchange=e=>nerve.visible=e.target.checked;
$('pathSkins').onchange=routeFilter;
$('opacity').oninput=e=>terrain.material.opacity=e.target.value/100;
$('deformation').oninput=e=>$('deformValue').textContent=e.target.value+'%';
$('pause').onclick=()=>{paused=!paused;$('pause').textContent=paused?'▶ Play':'Ⅱ Pause';};
$('phase').oninput=e=>{phase=e.target.value/1000;paused=true;$('pause').textContent='▶ Play';update();};
$('top').onclick=()=>{camera.position.set(0,65,.01);controls.target.set(0,3,0);};
$('reset').onclick=()=>{camera.position.set(38,33,-43);controls.target.set(0,3,0);};
$('capture').onclick=()=>{renderer.render(scene,camera);const a=document.createElement('a');a.href=canvas.toDataURL();a.download='chignolin-atlas.png';a.click();};
function update(){
 skins.forEach(s=>s.update(phase,$('skinAlpha').value/100,$('deformation').value/100,0));
 if(data&&selected>=0){const frames=data.routes[selected].moleculeFrames;const p=phase*(frames.length-1),i=Math.min(Math.floor(p),frames.length-2),w=p-i;
 showCartoon(frames[i].map((a,j)=>a.map((v,k)=>v*(1-w)+frames[i+1][j][k]*w)));}
}
function resize(){for(const [r,c,el] of [[renderer,camera,canvas],[miniRenderer,miniCamera,$('mini')]]){const b=el.getBoundingClientRect();r.setSize(b.width,b.height,false);c.aspect=b.width/b.height;c.updateProjectionMatrix();}}
new ResizeObserver(resize).observe(canvas);resize();
let lastInset=0;
function animate(t){requestAnimationFrame(animate);const dt=Math.min(.1,(t-previous)/1000);previous=t;
 if(!paused){phase=(phase+dt*.08)%1;$('phase').value=Math.round(phase*1000);}
 skins.forEach(s=>s.update(phase,$('skinAlpha').value/100,$('deformation').value/100,0));
 if(!paused&&t-lastInset>100){update();lastInset=t;}
 controls.update();renderer.render(scene,camera);miniRenderer.render(miniScene,miniCamera);
}requestAnimationFrame(animate);
init().catch(e=>{$('loading').textContent='Unable to load: '+e.message;console.error(e);});
