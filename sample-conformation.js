export function sampleConformation(rep,phase,smooth=true){
 const time=Math.max(0,Math.min(1,phase))*(rep.molecularFrames.length-1);
 const i=Math.floor(time),j=Math.min(i+1,rep.molecularFrames.length-1),f=smooth?time-i:0;
 const atoms=rep.molecularFrames[i].map((p,k)=>p.map((x,q)=>x+(rep.molecularFrames[j][k][q]-x)*f));
 const angles=rep.frameAngles[i].map((a,q)=>{const delta=((rep.frameAngles[j][q]-a+540)%360)-180;return ((a+delta*f+540)%360)-180;});
 return {atoms,angles,frame:rep.startPs+i+(smooth?f:0)};
}
