import * as THREE from 'three';
const elements=['C','C','O','N','C','C','C','O','N','C'];
const radii={C:.17,N:.155,O:.152};
const bonds=[[0,1],[1,2],[1,3],[3,4],[4,5],[4,6],[6,7],[6,8],[8,9]];
import {sampleConformation} from "./sample-conformation.js";
export function makeMorph(parent,edge,color,free){
 const root=new THREE.Group();parent.add(root);
 const sphere=new THREE.SphereGeometry(1,24,16),cylinder=new THREE.CylinderGeometry(.025,.025,1,10);
 const mats=elements.map(el=>new THREE.MeshStandardMaterial({color:el==='O'?0xff8c94:el==='N'?0x89aaff:color,roughness:.3,metalness:.15}));
 const atoms=mats.map(mat=>{const m=new THREE.Mesh(sphere,mat);root.add(m);return m;});
 const bondMat=new THREE.MeshStandardMaterial({color:0xc4d9dd,roughness:.4});
 const links=bonds.map(()=>{const m=new THREE.Mesh(cylinder,bondMat);root.add(m);return m;});
 function height(a){
  const x=(a[0]+180)/12-.5,z=(a[1]+180)/12-.5,ix=Math.floor(x),iz=Math.floor(z),fx=x-ix,fz=z-iz;
  const read=(i,j)=>free[(i+30)%30][(j+30)%30];
  return (read(ix,iz)*(1-fx)*(1-fz)+read(ix+1,iz)*fx*(1-fz)+read(ix,iz+1)*(1-fx)*fz+read(ix+1,iz+1)*fx*fz)*1.3+2.8;
 }
 return {root,update(phase,{smooth,spacefill,scale}){
  const s=sampleConformation(edge.representative,phase,smooth);
  root.position.set(s.angles[0]/12,height(s.angles),s.angles[1]/12);root.scale.setScalar(scale);
  atoms.forEach((m,i)=>{m.position.set(...s.atoms[i]);m.scale.setScalar(spacefill?radii[elements[i]]:.065);});
  links.forEach((m,k)=>{m.visible=!spacefill;if(spacefill)return;const [i,j]=bonds[k],a=atoms[i].position,b=atoms[j].position,dir=b.clone().sub(a);m.position.copy(a).add(b).multiplyScalar(.5);m.scale.y=dir.length();m.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),dir.normalize());});
  return s;
 }};
}
