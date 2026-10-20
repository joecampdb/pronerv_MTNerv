import * as THREE from 'three';
import {OrbitControls} from './OrbitControls.js';
import {createDynamics} from './dynamics.js';
import {backboneCartoon} from './cartoon.js';
const $=id=>document.getElementById(id);
const canvas=$('scene'), renderer=new THREE.WebGLRenderer({canvas,antialias:true,preserveDrawingBuffer:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.setClearColor(0x080e19,0);
renderer.outputColorSpace=THREE.SRGBColorSpace;
const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(42,1,.1,300);
camera.position.set(34,35,43);
const controls=new OrbitControls(camera,canvas);controls.target.set(0,3,0);controls.enableDamping=true;controls.maxDistance=110;controls.minDistance=12;controls.autoRotateSpeed=.35;
scene.add(new THREE.HemisphereLight(0xd5ffff,0x172032,2.1));
const key=new THREE.DirectionalLight(0xc9f7ff,3.2);key.position.set(-15,30,20);scene.add(key);
const rim=new THREE.DirectionalLight(0xffb89a,2);rim.position.set(20,12,-25);scene.add(rim);
const world=new THREE.Group();scene.add(world);
const palette=['#4cf1bc','#38b6d9','#7377da','#df8aaa','#ffce83'].map(c=>new THREE.Color(c));
function color(e){const f=Math.max(0,Math.min(3.999,e/8*4)),i=Math.floor(f);return palette[i].clone().lerp(palette[i+1],f-i);}
function label(text,pos){const c=document.createElement('canvas');c.width=256;c.height=64;const ctx=c.getContext('2d');ctx.fillStyle='#7b9baa';ctx.font='24px monospace';ctx.textAlign='center';ctx.fillText(text,128,40);const s=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(c),transparent:true}));s.position.set(...pos);s.scale.set(7,1.75,1);scene.add(s);}
const grid=new THREE.GridHelper(30,6,0x2b4657,0x182d3e);grid.position.y=-2.5;scene.add(grid);
label('φ / phi',[0,-2,18]);label('ψ / psi',[-19,-2,0]);label('−180°',[-15,-2,17]);label('+180°',[15,-2,17]);
let data,skin,nerve,faces,selected,playing=false,step=0,last=0,dynamics,previousTime=0;
const markers=[], ray=new THREE.Raycaster(), mouse=new THREE.Vector2();
const miniRenderer=new THREE.WebGLRenderer({canvas:$('mini'),antialias:true,alpha:true});miniRenderer.setPixelRatio(Math.min(devicePixelRatio,2));
const miniScene=new THREE.Scene(),miniCamera=new THREE.PerspectiveCamera(35,1,.01,100);miniCamera.position.set(1.5,1.2,2.7);miniCamera.lookAt(0,0,0);
miniScene.add(new THREE.HemisphereLight(0xffffff,0x26334a,3));const ml=new THREE.DirectionalLight(0xffffff,3);ml.position.set(2,3,2);miniScene.add(ml);
let molecule=new THREE.Group();miniScene.add(molecule);
const atomGeo=new THREE.SphereGeometry(.065,20,12),bondGeo=new THREE.CylinderGeometry(.018,.018,1,10),elements=['C','C','O','N','C','C','C','O','N','C'],bonds=[[0,1],[1,2],[1,3],[3,4],[4,5],[4,6],[6,7],[6,8],[8,9]];
const atomMats={C:new THREE.MeshStandardMaterial({color:0xa9ddce}),N:new THREE.MeshStandardMaterial({color:0x708efc}),O:new THREE.MeshStandardMaterial({color:0xf18e92})},bondMat=new THREE.MeshStandardMaterial({color:0x687f94});
function drawMol(coords){for(const o of molecule.children)if(o.userData.cartoon)o.traverse(x=>{x.geometry?.dispose();x.material?.dispose();});molecule.clear();coords.forEach((p,i)=>{const s=new THREE.Mesh(atomGeo,atomMats[elements[i]]);s.position.set(...p);molecule.add(s);});for(const [i,j]of bonds){const a=new THREE.Vector3(...coords[i]),b=new THREE.Vector3(...coords[j]),d=b.clone().sub(a);const c=new THREE.Mesh(bondGeo,bondMat);c.position.copy(a.add(b).multiplyScalar(.5));c.scale.y=d.length();c.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),d.normalize());molecule.add(c);}const cartoon=backboneCartoon(coords,[0,1,3,4,6,8,9],.025);cartoon.userData.cartoon=true;molecule.add(cartoon);}
function select(i){selected=i;const n=data.nodes[i];$('nodeSelect').value=i;drawMol(n.molecule);$('details').innerHTML=`<strong>{${n.simplex.map(x=>'U'+x).join(' ∩ ')}}</strong> · ${n.count.toLocaleString()} sampled witnesses<br>φ ${n.angles[0].toFixed(0)}° · ψ ${n.angles[1].toFixed(0)}° · ${n.energy.toFixed(2)} kBT<br><span class="small">Associated frame: run ${Math.floor(n.frame/250000)+1}, ${(n.frame%250000/1000).toFixed(3)} ns</span>`;markers.forEach((m,j)=>{m.scale.setScalar(j===i?1.8:1);m.material.emissiveIntensity=j===i?2:.5;});}
const tracer=new THREE.Mesh(new THREE.SphereGeometry(.28,16,12),new THREE.MeshBasicMaterial({color:0xffffff}));world.add(tracer);
const map=$('map'),ctx=map.getContext('2d');
function showFrame(i){step=i;const t=data.track[i];tracer.position.set(t.pos[0],t.pos[1]+1.4,t.pos[2]);$('scrub').value=i;$('time').textContent=`Run 1 · ${(t.frame/1000).toFixed(2)} ns`;
ctx.fillStyle='#09131f';ctx.fillRect(0,0,260,260);for(let x=0;x<30;x++)for(let y=0;y<30;y++){if(data.histogram[x][y]===0)continue;ctx.fillStyle='#'+color(data.freeEnergy[x][y]).getHexString();ctx.fillRect(x*260/30,260-(y+1)*260/30,9,9);}ctx.strokeStyle='#fff';ctx.lineWidth=2;ctx.beginPath();ctx.arc((t.angles[0]+180)/360*260,260-(t.angles[1]+180)/360*260,5,0,Math.PI*2);ctx.stroke();if(playing)drawMol(t.molecule);}
async function init(){
const responses=await Promise.all(['data.json','surface.bin','triangles.bin'].map(f=>fetch(f).then(r=>{if(!r.ok)throw Error(`${f}: ${r.status}`);return r;})));
data=await responses[0].json();const vertices=new Float32Array(await responses[1].arrayBuffer()),indices=new Uint32Array(await responses[2].arrayBuffer());
const count=vertices.length/7,p=new Float32Array(count*3),norm=new Float32Array(count*3),colors=new Float32Array(count*3);
for(let i=0;i<count;i++){p.set(vertices.subarray(i*7,i*7+3),i*3);norm.set(vertices.subarray(i*7+3,i*7+6),i*3);color(vertices[i*7+6]).toArray(colors,i*3);}
const geo=new THREE.BufferGeometry();geo.setAttribute('position',new THREE.BufferAttribute(p,3));geo.setAttribute('normal',new THREE.BufferAttribute(norm,3));geo.setAttribute('color',new THREE.BufferAttribute(colors,3));geo.setIndex(new THREE.BufferAttribute(indices,1));
skin=new THREE.Mesh(geo,new THREE.MeshStandardMaterial({vertexColors:true,metalness:.28,roughness:.4,side:THREE.DoubleSide,transparent:true,opacity:.6,depthWrite:false}));world.add(skin);
nerve=new THREE.Group();nerve.visible=$('nerve').checked;world.add(nerve);faces=new THREE.Group();nerve.add(faces);
const positions=data.nodes.map(n=>new THREE.Vector3(n.pos[0],n.pos[1]+2.1,n.pos[2]));
for(const [i,j]of data.edges){const geom=new THREE.BufferGeometry().setFromPoints([positions[i],positions[j]]);nerve.add(new THREE.Line(geom,new THREE.LineBasicMaterial({color:0xc8e9ee,transparent:true,opacity:.42})));}
const tri=[];for(const chain of data.chains)for(const i of chain)tri.push(...positions[i].toArray());const tg=new THREE.BufferGeometry();tg.setAttribute('position',new THREE.Float32BufferAttribute(tri,3));tg.computeVertexNormals();faces.add(new THREE.Mesh(tg,new THREE.MeshBasicMaterial({color:0xa1cddd,transparent:true,opacity:.07,side:THREE.DoubleSide,depthWrite:false})));
const nodeGeo=new THREE.IcosahedronGeometry(.17,1);
data.nodes.forEach((n,i)=>{const c=[0xa8ffdb,0x81bfff,0xffd29a][n.simplex.length-1];const m=new THREE.Mesh(nodeGeo,new THREE.MeshStandardMaterial({color:c,emissive:c,emissiveIntensity:.5}));m.position.copy(positions[i]);m.userData.index=i;nerve.add(m);markers.push(m);const option=document.createElement('option');option.value=i;option.textContent=`{ ${n.simplex.map(x=>'U'+x).join(' ∩ ')} }`; $('nodeSelect').append(option);});
$('objects').textContent=data.nodes.length;$('arrows').textContent=data.edges.length;$('chains').textContent=data.chains.length;select(0);showFrame(0);dynamics=await createDynamics(world,data.freeEnergy);$('loading').remove();
window.__atlas={frames:data.frames,representatives:data.representatives,nodes:data.nodes.length,triangles:data.chains.length,meshVertices:count,ready:true};
}
$('nodeSelect').onchange=e=>{playing=false;$('play').textContent='▶ Play';select(Number(e.target.value));};
$('skin').onchange=e=>skin.visible=e.target.checked;$('nerve').onchange=e=>nerve.visible=e.target.checked;$('membranes').onchange=e=>faces.visible=e.target.checked;
$('nerveQuick').onchange=e=>{nerve.visible=e.target.checked;$('nerve').checked=e.target.checked;};
$('nerve').onchange=e=>{nerve.visible=e.target.checked;$('nerveQuick').checked=e.target.checked;};
$('rotate').onchange=e=>controls.autoRotate=e.target.checked;
$('opacity').oninput=e=>{const o=e.target.value/100;skin.material.transparent=o<1;skin.material.opacity=o;skin.material.depthWrite=o===1;skin.material.needsUpdate=true;$('opacityValue').textContent=e.target.value+'%';};
$('height').oninput=e=>{world.scale.y=e.target.value/100;$('heightValue').textContent=(e.target.value/100).toFixed(1)+'×';};
function view(top=false){camera.position.set(...(top?[0,65,.01]:[34,35,43]));controls.target.set(0,3,0);controls.update();$('top').classList.toggle('active',top);$('perspective').classList.toggle('active',!top);}
$('top').onclick=()=>view(true);$('perspective').onclick=()=>view(false);$('reset').onclick=()=>{view();world.scale.y=1;$('height').value=100;$('heightValue').textContent='1.0×';};
$('play').onclick=()=>{playing=!playing;$('play').textContent=playing?'Ⅱ Pause':'▶ Play';if(!playing&&selected!==undefined)select(selected);};
$('scrub').oninput=e=>{showFrame(+e.target.value);drawMol(data.track[step].molecule);$('details').textContent='Actual trajectory conformation · run 1 · '+(data.track[step].frame/1000).toFixed(2)+' ns';};
$('capture').onclick=()=>{renderer.render(scene,camera);const a=document.createElement('a');a.download='alanine-molecular-landscape.png';a.href=canvas.toDataURL('image/png');a.click();};
let down;
canvas.addEventListener('pointerdown',e=>down=[e.clientX,e.clientY]);
canvas.addEventListener('pointerup',e=>{if(!down||Math.hypot(e.clientX-down[0],e.clientY-down[1])>5||!nerve?.visible)return;const r=canvas.getBoundingClientRect();mouse.set((e.clientX-r.left)/r.width*2-1,-(e.clientY-r.top)/r.height*2+1);ray.setFromCamera(mouse,camera);const hits=ray.intersectObjects(markers);if(hits.length){playing=false;$('play').textContent='▶ Play';select(hits[0].object.userData.index);}});
function resize(){let r=canvas.getBoundingClientRect();renderer.setSize(r.width,r.height,false);camera.aspect=r.width/r.height;camera.updateProjectionMatrix();r=$('mini').getBoundingClientRect();miniRenderer.setSize(r.width,r.height,false);miniCamera.aspect=r.width/r.height;miniCamera.updateProjectionMatrix();}
new ResizeObserver(resize).observe(canvas.parentElement);resize();
function animate(t){requestAnimationFrame(animate);controls.update();const dt=Math.min(.1,(t-previousTime)/1000);previousTime=t;dynamics?.tick(dt);if(playing&&data&&t-last>100){showFrame((step+1)%data.track.length);$('details').textContent='Actual trajectory conformation · run 1 · '+(data.track[step].frame/1000).toFixed(2)+' ns';last=t;}molecule.rotation.y+=.002;renderer.render(scene,camera);miniRenderer.render(miniScene,miniCamera);}requestAnimationFrame(animate);
init().catch(e=>{$('loading').textContent='Unable to load the landscape: '+e.message;console.error(e);});
