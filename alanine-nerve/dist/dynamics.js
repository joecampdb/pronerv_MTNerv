import * as THREE from 'three';
import {makeMorph} from './morph.js';
import {loadPathSkins} from './path-skins.js';
const $=id=>document.getElementById(id);
const COLORS=[0x9dffcc,0xffcf83,0xb9a1ff,0xff8f9e];
export async function createDynamics(world,freeEnergy){
 const res=await fetch('./dynamics.json');if(!res.ok)throw Error('Cannot load dynamics');const d=await res.json();
 const group=new THREE.Group();world.add(group);
 const routes=new THREE.Group(),composition=new THREE.Group();group.add(routes,composition);
 let enabled=true,paused=false,clock=0,selected=-1;
 const particles=[],lines=[],molecules=[];
 let activeEdges=null,frozenPhase=null;
 const v=p=>new THREE.Vector3(...p);
 function textSprite(text,position,c){
  const canvas=document.createElement('canvas');canvas.width=256;canvas.height=80;const ctx=canvas.getContext('2d');
  ctx.fillStyle='#0b1423';ctx.roundRect(8,5,240,64,14);ctx.fill();ctx.strokeStyle='#'+new THREE.Color(c).getHexString();ctx.lineWidth=2;ctx.stroke();
  ctx.fillStyle='#e5fff5';ctx.font='bold 27px system-ui';ctx.textAlign='center';ctx.fillText(text,128,48);
  const s=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(canvas),depthTest:false}));s.position.copy(position);s.scale.set(4.5,1.4,1);s.renderOrder=8;group.add(s);
 }
 d.basins.forEach(b=>{
  const p=v(b.pos);const ring=new THREE.Mesh(new THREE.TorusGeometry(.46,.07,8,36),new THREE.MeshBasicMaterial({color:COLORS[b.id]}));ring.rotation.x=Math.PI/2;ring.position.copy(p);group.add(ring);
  textSprite(`${b.name} · ${(100*b.occupancy).toFixed(1)}%`,p.clone().add(new THREE.Vector3(0,1.1,0)),COLORS[b.id]);
 });
 const dotGeometry=new THREE.SphereGeometry(.10,10,8),coneGeometry=new THREE.ConeGeometry(.18,.5,10);
 function makePath(edge){
  // Actual core passage, plus clearly disclosed center-to-core display connectors.
  const points=[v(d.basins[edge.source].pos),...edge.representative.positions.map(v),v(d.basins[edge.target].pos)];
  const visible=[];for(let k=1;k<points.length;k++){
   if(Math.abs(points[k].x-points[k-1].x)>15||Math.abs(points[k].z-points[k-1].z)>15)continue;
   visible.push(...points[k-1].toArray(),...points[k].toArray());
  }
  const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.Float32BufferAttribute(visible,3));
  const material=new THREE.LineBasicMaterial({color:COLORS[edge.source],transparent:true,opacity:.65});
  const line=new THREE.LineSegments(geometry,material);routes.add(line);lines.push(line);
  // Cumulative path parameter, excluding false straight lines across the periodic seam.
  const segments=[];let length=0;
  for(let k=1;k<points.length;k++){
   if(Math.abs(points[k].x-points[k-1].x)>15||Math.abs(points[k].z-points[k-1].z)>15)continue;
   const len=points[k].distanceTo(points[k-1]);if(len<1e-6)continue;
   segments.push({a:points[k-1],b:points[k],start:length,len});length+=len;
  }
  function at(f){const distance=f*length;const s=segments.find(s=>distance<=s.start+s.len)||segments.at(-1);return {p:s.a.clone().lerp(s.b,Math.max(0,Math.min(1,(distance-s.start)/s.len))),direction:s.b.clone().sub(s.a).normalize()};}
  const mat=new THREE.MeshBasicMaterial({color:COLORS[edge.source],depthTest:false});
  // Log-scaled density exposes rare routes; speed is intentionally not a rate estimate.
  const n=2+Math.floor(Math.log10(edge.count+1)*2);
  for(let k=0;k<n;k++){const m=new THREE.Mesh(k===0?coneGeometry:dotGeometry,mat);m.renderOrder=6;routes.add(m);particles.push({mesh:m,edge:edge.id,at,phase:k/n,arrow:k===0});}
 }
 d.edges.forEach(makePath);
 d.edges.forEach(e=>molecules.push(makeMorph(group,e,COLORS[e.source],freeEnergy)));
 const skins=await loadPathSkins(group,d.edges.map(e=>COLORS[e.source]));
 function visibleMotion(ids=null){
  activeEdges=ids;
  particles.forEach(p=>p.mesh.visible=$('particles').checked&&(!ids||ids.includes(p.edge)));
  molecules.forEach((m,i)=>m.root.visible=$('molecules').checked&&(!ids||ids.includes(i)));
  skins.forEach((s,i)=>s.mesh.visible=$('pathSkins').checked&&(!ids||ids.includes(i)));
  lines.forEach(l=>l.visible=$('guideLines').checked);
 }
 function renderMolecules(){
  const phase=frozenPhase??(clock/5%1),smooth=$('interpolation').value==='smooth';
  skins.forEach((s,i)=>s.update(selected>=0?phase:(phase+i*.137)%1,Number($('skinAlpha').value)/100,Number($('deformation').value)/100,$('skinHighlight').checked?1:0));
  if(selected>=0&&!$('molecules').checked){$('morphTime').textContent=`Visual deformation phase ${phase.toFixed(2)} · MD-attached material warp`;}
  molecules.forEach((m,i)=>{
   if(!m.root.visible)return;
   const f=selected>=0?phase:(phase+i*.137)%1;
   const s=m.update(f,{smooth,spacefill:$('moleculeStyle').value==='spacefill',scale:Number($('moleculeScale').value)});
   if(i===selected)$('morphTime').textContent=`Run ${d.edges[i].representative.run} · ${s.frame.toFixed(2)} ps · ${smooth?'interpolated':'recorded frame'}`;
  });
  if(selected<0)$('morphTime').textContent='Independent route excerpts · normalized playback';
  $('morphPhase').value=Math.round(phase*1000);
 }
 function stats(){
  const lag=$('lag').value,m=d.lagModels[lag];
  if(selected<0){$('flowDetails').innerHTML=`<strong>${d.edges.length} observed directed routes · ${d.chains.length} composable pairs</strong><br>${d.edges.reduce((s,e)=>s+e.count,0).toLocaleString()} core-to-core passages across 750 ns.<br><span class="small">Particle density is logarithmic in passage count; playback speed is illustrative. Both directions are shown.</span>`;return;}
  const e=d.edges[selected],a=d.basins[e.source],b=d.basins[e.target],p=m.probabilities[e.source][e.target];
  $('flowDetails').innerHTML=`<strong>${a.name} → ${b.name} · ${e.count.toLocaleString()} passages${e.count<10?' · sparse evidence':''}</strong><br>Per run: ${e.perRunCounts.join(' / ')}<br>P(${b.name} | ${a.name}; ${lag} ps) = ${(p*100).toFixed(3)}%<br>Gross frequency: ${e.grossEventsPerNs.toFixed(3)} events/ns<br>Median core-passage duration: ${e.medianDurationPs} ps<br><span class="small">Displayed route: run ${e.representative.run}, ${(e.representative.startPs/1000).toFixed(3)}–${(e.representative.endPs/1000).toFixed(3)} ns. Short center-to-core connectors are schematic.</span>`;
 }
 function filter(){
  selected=Number($('route').value);
  lines.forEach((l,i)=>{l.material.opacity=(selected<0||i===selected) ? .8 : .08;});
  visibleMotion(selected<0?null:[selected]);stats();renderMolecules();
 }
 d.edges.forEach(e=>{const o=document.createElement('option');o.value=e.id;o.textContent=`${d.basins[e.source].name} → ${d.basins[e.target].name} · ${e.count.toLocaleString()} passages`;$('route').append(o);});
 d.chains.forEach(([x,y],i)=>{const a=d.edges[x],b=d.edges[y];const o=document.createElement('option');o.value=i;o.textContent=`${d.basins[a.source].name} → ${d.basins[a.target].name} → ${d.basins[b.target].name}`;$('pathChain').append(o);});
 function clearComposition(){while(composition.children.length){const c=composition.children[0];composition.remove(c);c.geometry?.dispose();c.material?.dispose();}}
 function selectChain(){
  clearComposition();const index=Number($('pathChain').value);
  if(index<0){$('chainDetails').textContent='Select a two-step chain to see a dynamic nerve 2-simplex.';filter();return;}
  $('route').value='-1';selected=-1;stats();
  const [x,y]=d.chains[index],a=d.edges[x],b=d.edges[y],ids=[a.source,a.target,b.target];
  const points=ids.map(i=>v(d.basins[i].pos).add(new THREE.Vector3(0,1.6,0)));
  lines.forEach((l,i)=>l.material.opacity=i===x||i===y?1:.07);
  visibleMotion([x,y]);renderMolecules();
  if(ids[0]!==ids[2]){
   const g=new THREE.BufferGeometry().setFromPoints(points);g.setIndex([0,1,2]);g.computeVertexNormals();composition.add(new THREE.Mesh(g,new THREE.MeshBasicMaterial({color:0xffe6b2,side:THREE.DoubleSide,transparent:true,opacity:.18,depthWrite:false})));
  }
  const composite=ids[0]===ids[2]
   ?Array.from({length:65},(_,k)=>points[0].clone().add(new THREE.Vector3(Math.sin(k/64*Math.PI*2)*1.5,1-Math.cos(k/64*Math.PI*2),0)))
   :[points[0],points[2]];
  const line=new THREE.Line(new THREE.BufferGeometry().setFromPoints(composite),new THREE.LineDashedMaterial({color:0xfff1b1,dashSize:.32,gapSize:.22,depthTest:false}));line.computeLineDistances();composition.add(line);
  $('chainDetails').innerHTML=`<strong>${ids.map(i=>d.basins[i].name).join(' → ')}</strong><br>Dashed ${d.basins[ids[0]].name} → ${d.basins[ids[2]].name}: formal composite of these two arrows${ids[0]===ids[2]?', a return path, not an identity':''}.<br><span class="small">Composition asserts concatenability, not a separately observed direct transition or an observed consecutive pair. The membrane is categorical, not a sampled transition surface.</span>`;
 }
 $('flow').onchange=e=>{enabled=e.target.checked;group.visible=enabled;};
 $('flowPause').onclick=()=>{paused=!paused;if(!paused)frozenPhase=null;$('flowPause').textContent=paused?'▶ Resume flow':'Ⅱ Pause flow';};
 $('route').onchange=()=>{$('pathChain').value='-1';clearComposition();$('chainDetails').textContent='Select a two-step chain to see a dynamic nerve 2-simplex.';filter();};
 $('lag').onchange=stats;$('pathChain').onchange=selectChain;
 $('pathSkins').onchange=$('guideLines').onchange=$('molecules').onchange=$('particles').onchange=()=>{visibleMotion(activeEdges);renderMolecules();};
 $('skinAlpha').oninput=()=>{$('skinAlphaValue').textContent=$('skinAlpha').value+'%';renderMolecules();};
 $('deformation').oninput=()=>{$('deformValue').textContent=$('deformation').value+'%';renderMolecules();};
 $('skinHighlight').onchange=renderMolecules;
 $('interpolation').onchange=$('moleculeStyle').onchange=$('moleculeScale').oninput=renderMolecules;
 $('morphPhase').oninput=e=>{paused=true;$('flowPause').textContent='▶ Resume flow';frozenPhase=Number(e.target.value)/1000;clock=frozenPhase*5;renderMolecules();};
 $('flowLegend').innerHTML=d.basins.map(b=>`<span style="color:#${new THREE.Color(COLORS[b.id]).getHexString()}">${b.name}: (${b.angles.join('°, ')}°)</span>`).join(' · ');
 $('route').value='-1';filter();
 return {tick(dt){if(!enabled||paused)return;clock+=dt*Number($('flowSpeed').value)/100;renderMolecules();for(const p of particles){if(!p.mesh.visible)continue;const state=p.at((clock/5+p.phase)%1);p.mesh.position.copy(state.p);if(p.arrow)p.mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),state.direction);}},data:d};
}
