import * as THREE from 'three';
export async function loadPathSkins(parent,colors){
 const meta=await fetch('./skins/index.json').then(r=>{if(!r.ok)throw Error('Skin metadata missing');return r.json();});
 return Promise.all(meta.map(async entry=>{
  const [vb,ib,mb]=await Promise.all([`${entry.id}.bin`,`${entry.id}-indices.bin`,`${entry.id}-morph.bin`].map(f=>fetch('./skins/'+f).then(r=>{if(!r.ok)throw Error('Skin geometry missing');return r.arrayBuffer();})));
  const data=new Float32Array(vb),geo=new THREE.BufferGeometry(),interleaved=new THREE.InterleavedBuffer(data,7);
  geo.setAttribute('position',new THREE.InterleavedBufferAttribute(interleaved,3,0));
  geo.setAttribute('normal',new THREE.InterleavedBufferAttribute(interleaved,3,3));
  geo.setAttribute('passageTime',new THREE.InterleavedBufferAttribute(interleaved,1,6));
  geo.setIndex(new THREE.BufferAttribute(new Uint32Array(ib),1));
  const morphData=new Float32Array(mb);
  geo.morphAttributes.position=[];geo.morphAttributes.normal=[];
  for(let k=0;k<entry.morphFrames;k++){
   const p=new Float32Array(entry.vertices*3),n=new Float32Array(entry.vertices*3);
   for(let i=0;i<entry.vertices;i++){const start=(k*entry.vertices+i)*6;p.set(morphData.subarray(start,start+3),i*3);n.set(morphData.subarray(start+3,start+6),i*3);}
   geo.morphAttributes.position.push(new THREE.BufferAttribute(p,3));geo.morphAttributes.normal.push(new THREE.BufferAttribute(n,3));
  }
  const phase={value:0},opacity={value:.58};
  const material=new THREE.MeshStandardMaterial({color:colors[entry.id],emissive:colors[entry.id],emissiveIntensity:.15,
    transparent:true,opacity:.58,roughness:.27,metalness:.12,side:THREE.DoubleSide,depthWrite:false});
  material.onBeforeCompile=shader=>{
   shader.uniforms.skinPhase=phase;shader.uniforms.skinOpacity=opacity;
   shader.vertexShader='attribute float passageTime;\nvarying float vPassageTime;\n'+shader.vertexShader;
   shader.vertexShader=shader.vertexShader.replace('#include <begin_vertex>','#include <begin_vertex>\nvPassageTime = passageTime;');
   shader.fragmentShader='uniform float skinPhase;\nuniform float skinOpacity;\nvarying float vPassageTime;\n'+shader.fragmentShader;
   shader.fragmentShader=shader.fragmentShader.replace('#include <color_fragment>',`#include <color_fragment>
    float progressDistance = abs(vPassageTime - skinPhase);
    float pulse = exp(-pow(progressDistance / 0.10, 2.0));
    diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.84, 1.0, 0.94), pulse * 0.65);
    diffuseColor.a = skinOpacity * (0.58 + 0.42 * pulse);`);
   shader.fragmentShader=shader.fragmentShader.replace('#include <emissivemap_fragment>','#include <emissivemap_fragment>\ntotalEmissiveRadiance += diffuseColor.rgb * pulse * 0.45;');
  };
  const mesh=new THREE.Mesh(geo,material);mesh.renderOrder=2;parent.add(mesh);
  return {mesh,update(time,alpha,amount=1){
   phase.value=time;opacity.value=alpha;
   const f=(time%1)*entry.morphFrames,i=Math.floor(f),w=f-i;
   mesh.morphTargetInfluences.fill(0);
   mesh.morphTargetInfluences[i]=(1-w)*amount;
   mesh.morphTargetInfluences[(i+1)%entry.morphFrames]+=w*amount;
  }};
 }));
}
