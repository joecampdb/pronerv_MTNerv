"""Blender 4.0/Cycles: measured heights, recorded molecular relief, nerve overlay.
No continuous molecular surface, interpolated conformer or physical clock implied.
"""
import bpy,json,colorsys,math,sys
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'paper/figures'
sys.path.insert(0,str(Path(__file__).resolve().parent))
from camera_fit import fit_camera
def material(name,c,rough=.35,metal=.1,alpha=1):
 m=bpy.data.materials.new(name);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal;p.inputs['Coat Weight'].default_value=.3
 if alpha<1:
  ns=m.node_tree.nodes;ls=m.node_tree.links;t=ns.new('ShaderNodeBsdfTransparent');mix=ns.new('ShaderNodeMixShader');mix.inputs[0].default_value=alpha;ls.new(t.outputs[0],mix.inputs[1]);ls.new(p.outputs[0],mix.inputs[2]);ls.new(mix.outputs[0],ns.get('Material Output').inputs[0])
 return m
def tube(name,points,mat,radius):
 c=bpy.data.curves.new(name,'CURVE');c.dimensions='3D';c.bevel_depth=radius;c.bevel_resolution=2;s=c.splines.new('POLY');s.points.add(len(points)-1)
 for p,x in zip(s.points,points):p.co=(*x,1)
 o=bpy.data.objects.new(name,c);bpy.context.scene.collection.objects.link(o);o.data.materials.append(mat)
def mesh(name,points,faces,mat):
 m=bpy.data.meshes.new(name);m.from_pydata(points,[],faces);m.update();o=bpy.data.objects.new(name,m);bpy.context.scene.collection.objects.link(o);o.data.materials.append(mat);return o
for name in ['alanine','chignolin']:
 bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
 d=json.loads((ROOT/f'dist/validation/{name}-atlas.json').read_text());r=json.loads((ROOT/f'dist/validation/{name}-recorded.json').read_text());h=d['height'];n=h['bins'];lo,hi=h['limits'];maximum=max(h['height_nm'][i][j] for i in range(n) for j in range(n) if h['supported'][i][j]);scale=10/maximum
 def pos(q,v,lift=0):return ((q[0]-lo[0])/(hi[0]-lo[0])*30-15,(q[1]-lo[1])/(hi[1]-lo[1])*30-15,v*scale+lift)
 pale=material('Nerve edges',(.65,.8,.85),.25,.15);plate=material('Nerve plates',(.55,.8,.9),.28,0,.07);bond=material('Recorded site connections',(.18,.3,.35),.3,.2)
 site=[material('Recorded site '+str(i),colorsys.hsv_to_rgb(.58-.48*i/9,.6,.7),.24,.25) for i in range(10)]
 for i in range(n):
  for j in range(n):
   if not h['supported'][i][j]:continue
   v=h['height_nm'][i][j];points=[pos([lo[0]+(i+a)/n*(hi[0]-lo[0]),lo[1]+(j+b)/n*(hi[1]-lo[1])],v) for a,b in [(0,0),(1,0),(1,1),(0,1)]]
   mesh('Supported mobility tile',points,[(0,1,2,3)],material('Mobility',colorsys.hsv_to_rgb(.47-.39*v/maximum,.65,.65),.45,.08))
 for a in r['anchors']:
  i,j=a['bin'];origin=Vector(pos(a['chart'],h['height_nm'][i][j],.3));factor=1.4 if name=='alanine' else .65
  points=[origin+Vector((p[0],p[2],p[1]))*factor for p in a['coords_nm']]
  for k,p in enumerate(points):
   bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=.06,location=p);bpy.context.object.data.materials.append(site[k])
  for a,b in r['bonds']:tube('Recorded bond guide',[points[a],points[b]],bond,.025)
 nodes=d['cover']['nodes'];positions=[pos(a['chart'],a['height_nm'],2) if a['supported'] else None for a in nodes]
 def allowed(ids):return all(positions[i] for i in ids) and not(name=='alanine' and any(max(nodes[i]['chart'][k] for i in ids)-min(nodes[i]['chart'][k] for i in ids)>180 for k in [0,1]))
 for a,b in d['cover']['edges']:
  if allowed([a,b]):tube('Inclusion',[positions[a],positions[b]],pale,.018)
 for ids in d['cover']['chains']:
  if allowed(ids):mesh('Inclusion chain',[positions[i] for i in ids],[(0,1,2)],plate)
 for p in positions:
  if p:
   bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=.09,location=p);bpy.context.object.data.materials.append(pale)
 s=bpy.context.scene;s.render.engine='CYCLES';s.cycles.samples=48;s.cycles.use_denoising=True
 prefs=bpy.context.preferences.addons['cycles'].preferences
 try:
  prefs.compute_device_type='OPTIX';prefs.get_devices()
  for device in prefs.devices:device.use=device.type=='OPTIX'
  s.cycles.device='GPU'
 except Exception:s.cycles.device='CPU'
 s.world.use_nodes=True;s.world.node_tree.nodes['Background'].inputs['Color'].default_value=(.025,.035,.05,1);s.world.node_tree.nodes['Background'].inputs['Strength'].default_value=.4
 s.view_settings.view_transform='AgX';s.view_settings.look='AgX - Medium High Contrast';s.view_settings.exposure=.2
 for location,power,size in [((0,-15,32),13000,16),((-18,10,24),16000,14),((20,20,18),18000,12)]:
  bpy.ops.object.light_add(type='AREA',location=location);o=bpy.context.object;o.data.energy=power;o.data.shape='RECTANGLE';o.data.size=size;o.data.size_y=5;o.rotation_euler=(Vector((0,0,5))-o.location).to_track_quat('-Z','Y').to_euler()
 bpy.ops.object.camera_add(location=(35,-40,32));s.camera=bpy.context.object;s.camera.rotation_euler=(Vector((0,0,5))-s.camera.location).to_track_quat('-Z','Y').to_euler();s.camera.data.type='ORTHO';s.camera.data.ortho_scale=37
 s.render.resolution_x=1500;s.render.resolution_y=1050;s.render.resolution_percentage=100;s.render.image_settings.file_format='PNG';s.render.filepath=str(OUT/(name+'-measured-landscape.png'))
 fit_camera(s)
 s['scientific_scope']='Mobility tile heights in nm with fixed visual scale; recorded molecular sites under rigid alignment; lifted nerve; no smooth molecular deformation law.'
 s['height_scale_visual_units_per_nm']=scale
 dest=ROOT/'output/measured-scenes';dest.mkdir(exist_ok=True,parents=True);bpy.ops.wm.save_as_mainfile(filepath=str(dest/(name+'.blend')));bpy.ops.render.render(write_still=True)
