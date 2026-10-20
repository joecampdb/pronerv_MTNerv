import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {sampleConformation} from './dist/sample-conformation.js';
const data=JSON.parse(readFileSync(new URL('./dist/dynamics.json',import.meta.url)));
for(const e of data.edges){
 const r=e.representative,n=r.molecularFrames.length;
 assert.deepEqual(sampleConformation(r,0).atoms,r.molecularFrames[0]);
 assert.deepEqual(sampleConformation(r,1).atoms,r.molecularFrames[n-1]);
 for(let k=0;k<n;k++){
  const sample=sampleConformation(r,k/(n-1),true);
  assert(Math.abs(sample.frame-(r.startPs+k))<1e-9);
  sample.atoms.flat().forEach((x,i)=>assert(Math.abs(x-r.molecularFrames[k].flat()[i])<1e-10));
 }
 assert.deepEqual(sampleConformation(r,.5/(n-1),false).atoms,r.molecularFrames[0]);
}
const seam={startPs:0,molecularFrames:[[[0,0,0]],[[2,4,6]]],frameAngles:[[179,-179],[-179,179]]};
const halfway=sampleConformation(seam,.5);
assert.deepEqual(halfway.atoms,[[1,2,3]]);
assert(halfway.angles.every(a=>Math.abs(a)===180));
console.log('PASS: exact sampled-frame recovery, endpoints, recorded-frame mode and shortest periodic angular interpolation');
