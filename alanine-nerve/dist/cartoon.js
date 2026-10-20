import * as THREE from 'three';

/** Backbone trace cartoon; no inferred helix/sheet assignment. Coordinates in nm. */
export function backboneCartoon(coords, indices = coords.map((_,i)=>i), radius=.035) {
  const group=new THREE.Group();
  const points=indices.map(i=>new THREE.Vector3(...coords[i]));
  const curve=new THREE.CatmullRomCurve3(points,false,'centripetal');
  const geometry=new THREE.TubeGeometry(curve,100,radius,8,false);
  const colors=[];
  for(let i=0;i<geometry.attributes.position.count;i++){
    const t=Math.floor(i/9)/100;
    const c=new THREE.Color().setHSL(.58-.48*t,.65,.62);
    colors.push(c.r,c.g,c.b);
  }
  geometry.setAttribute('color',new THREE.Float32BufferAttribute(colors,3));
  group.add(new THREE.Mesh(geometry,new THREE.MeshStandardMaterial({vertexColors:true,roughness:.3})));
  for(const [j,i] of indices.entries()){
    const dot=new THREE.Mesh(new THREE.SphereGeometry(radius*1.5,12,8),
      new THREE.MeshStandardMaterial({color:new THREE.Color().setHSL(.58-.48*j/(indices.length-1),.65,.62)}));
    dot.position.set(...coords[i]);group.add(dot);
  }
  return group;
}

export function disposeGroup(group) {
  group.traverse(o=>{o.geometry?.dispose();if(o.material){for(const m of [].concat(o.material))m.dispose();}});
  group.clear();
}
