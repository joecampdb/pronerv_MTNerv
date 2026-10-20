"""Blender 4.0 / Eevee figures from the viewer's exact meshes and morph targets."""
import bpy, json, math, sys
import numpy as np
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"paper/figures"
CHIG="--chignolin" in sys.argv
DATA=ROOT/("dist/chignolin" if CHIG else "dist")
PREFIX="chignolin-" if CHIG else ""
bpy.ops.object.select_all(action="SELECT");bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
scene.render.engine="BLENDER_EEVEE"
scene.eevee.use_gtao=True;scene.eevee.gtao_distance=3
scene.eevee.taa_render_samples=64
scene.render.resolution_x=1600;scene.render.resolution_y=1050;scene.render.resolution_percentage=100
scene.render.image_settings.file_format="PNG"
scene.world.use_nodes=True
scene.world.node_tree.nodes["Background"].inputs["Color"].default_value=(.008,.016,.028,1)
scene.world.node_tree.nodes["Background"].inputs["Strength"].default_value=.6
scene.view_settings.exposure=.6
scene.view_settings.view_transform="Standard"
scene.view_settings.look="Medium High Contrast"
def xyz(p): return (float(p[0]),float(p[2]),float(p[1]))
def mat(name,color,alpha=1):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,alpha);m.use_nodes=True
    bs=m.node_tree.nodes.get("Principled BSDF");bs.inputs["Base Color"].default_value=(*color,1)
    bs.inputs["Roughness"].default_value=.34;bs.inputs["Metallic"].default_value=.12
    bs.inputs["Alpha"].default_value=alpha;m.blend_method="BLEND";m.use_screen_refraction=True
    m.show_transparent_back=False
    return m
def mesh(name,p,f,material):
    me=bpy.data.meshes.new(name);me.from_pydata([xyz(x) for x in p],[],[tuple(map(int,row[[0,2,1]])) for row in f]);me.update()
    obj=bpy.data.objects.new(name,me);scene.collection.objects.link(obj);obj.data.materials.append(material)
    for poly in me.polygons:poly.use_smooth=True
    return obj
data=json.loads((DATA/"data.json").read_text(encoding="utf-8"));dyn=({"edges":data["routes"],"basins":data["basins"]} if CHIG else json.loads((DATA/"dynamics.json").read_text()))
raw=np.fromfile(DATA/"surface.bin",dtype="<f4").reshape(-1,7)
faces=np.fromfile(DATA/"triangles.bin",dtype="<u4").reshape(-1,3)
terrain=mesh("MD occupancy terrain",raw[:,:3],faces,mat("Terrain",(.25,.5,.65),.72))
attr=terrain.data.color_attributes.new(name="energy",type="FLOAT_COLOR",domain="POINT")
palette=np.array([[.15,.85,.6],[.16,.55,.8],[.4,.35,.75],[.8,.4,.58],[1,.75,.4]])
for idx,e in enumerate(raw[:,6]):
    q=min(3.999,max(0,float(e)/8*4));i=int(q);c=palette[i]*(1-(q-i))+palette[i+1]*(q-i)
    attr.data[idx].color=(*c,1)
node=terrain.data.materials[0].node_tree.nodes.new("ShaderNodeVertexColor");node.layer_name="energy"
terrain.data.materials[0].node_tree.links.new(node.outputs["Color"],terrain.data.materials[0].node_tree.nodes.get("Principled BSDF").inputs["Base Color"])
colors=[(.3,1,.7),(1,.7,.3),(.62,.45,1),(1,.4,.5)]
metas=json.loads((DATA/"skins/index.json").read_text());skins=[];targets=[]
for e,m in zip(dyn["edges"],metas):
    base=np.fromfile(DATA/f'skins/{e["id"]}.bin',dtype="<f4").reshape(-1,7)
    f=np.fromfile(DATA/f'skins/{e["id"]}-indices.bin',dtype="<u4").reshape(-1,3)
    target=np.fromfile(DATA/f'skins/{e["id"]}-morph.bin',dtype="<f4").reshape(m["morphFrames"],m["vertices"],6)
    obj=mesh(f'Route {e["source"]} to {e["target"]}',base[:,:3],f,mat(f'Skin {e["id"]}',colors[e["source"]],.6))
    obj.shape_key_add(name="Basis")
    for k,t in enumerate(target):
        key=obj.shape_key_add(name=f"MD warp {k:02d}")
        coords=t[:,:3][:,[0,2,1]].astype(float).ravel()
        key.data.foreach_set("co",coords)
    skins.append(obj);targets.append(target)
def set_phase(t):
    for idx,obj in enumerate(skins):
        keys=obj.data.shape_keys.key_blocks
        for key in list(keys)[1:]:key.value=0
        q=(t%1)*12;k=int(q);w=q-k
        keys[k+1].value=1-w;keys[(k+1)%12+1].value=w
    scene.frame_set(scene.frame_current)
nerve_objects=[]
nerve_mat=mat("Nerve silver",(.78,.9,1),.55)
nerve_bs=nerve_mat.node_tree.nodes.get("Principled BSDF")
nerve_bs.inputs["Emission Color"].default_value=(.65,.8,1,1)
nerve_bs.inputs["Emission Strength"].default_value=.5
def line(name,points,material,radius=.024):
    curve=bpy.data.curves.new(name,"CURVE");curve.dimensions="3D";curve.bevel_depth=radius;curve.bevel_resolution=1
    poly=curve.splines.new("POLY");poly.points.add(len(points)-1)
    for p,v in zip(poly.points,points):p.co=(*xyz(v),1)
    o=bpy.data.objects.new(name,curve);scene.collection.objects.link(o);o.data.materials.append(material);return o
positions=[np.array(n["pos"])+[0,2.1,0] for n in data["nodes"]]
for i,j in data["edges"]:nerve_objects.append(line("Inclusion", [positions[i],positions[j]],nerve_mat))
for p in positions:
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=.11,location=xyz(p));o=bpy.context.object;o.data.materials.append(nerve_mat);nerve_objects.append(o)
bpy.ops.object.camera_add(location=(38,-44,34));camera=bpy.context.object;scene.camera=camera
def aim(point):camera.rotation_euler=(Vector(point)-camera.location).to_track_quat("-Z","Y").to_euler()
camera.data.type="ORTHO";camera.data.ortho_scale=45;aim((0,0,3.5))
for loc,power,size in [((0,-10,32),2400,20),((-20,10,20),1800,16),((20,20,12),1500,12)]:
    bpy.ops.object.light_add(type="AREA",location=loc);l=bpy.context.object;l.data.energy=power;l.data.shape="DISK";l.data.size=size;l.rotation_euler=(Vector((0,0,3))-l.location).to_track_quat("-Z","Y").to_euler()
labels=[]
for b in dyn["basins"]:
    p=np.array(b["pos"])+[0,1.5,0]
    bpy.ops.object.text_add(location=xyz(p));o=bpy.context.object;o.data.body=b["name"];o.data.align_x="CENTER";o.data.size=.85
    o.rotation_euler=camera.rotation_euler
    lm=mat("Label "+b["name"],(.9,.98,1))
    lm.node_tree.nodes.get("Principled BSDF").inputs["Emission Color"].default_value=(.9,.98,1,1)
    lm.node_tree.nodes.get("Principled BSDF").inputs["Emission Strength"].default_value=1
    o.data.materials.append(lm);labels.append(o)
set_phase(.18)
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/("paper/"+PREFIX+"molecular-landscape.blend")))
scene.render.filepath=str(OUT/(PREFIX+"landscape-nerve.png"));bpy.ops.render.render(write_still=True)
for o in nerve_objects+labels:o.hide_render=True
for i,o in enumerate(skins):o.hide_render=i!=1
terrain.hide_render=True
scene.render.resolution_x=1000;scene.render.resolution_y=850
all_positions=targets[1][:,:,:3].reshape(-1,3)[:,[0,2,1]]
center=(all_positions.min(0)+all_positions.max(0))/2
camera.location=Vector(center)+Vector((28,-35,28));aim(center)
rotation=np.array(camera.rotation_euler.to_matrix())
projected=(all_positions-center)@rotation
extent=np.ptp(projected,axis=0)
camera.data.ortho_scale=max(extent[0],extent[1]*1000/850)*1.15
for name,t in [("phase-0",0),("phase-1",1/3),("phase-2",2/3)]:
    set_phase(t);scene.render.filepath=str(OUT/(PREFIX+name+".png"));bpy.ops.render.render(write_still=True)
print("Rendered overview and three actual geometry-deformation snapshots.")
