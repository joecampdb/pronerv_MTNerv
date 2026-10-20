"""Blender cartoons from recorded MD coordinates, without secondary-structure claims."""
import bpy
import json
import numpy as np
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "paper/figures"
alanine = json.loads((ROOT/"dist/data.json").read_text())["nodes"][0]["molecule"]
chig = json.loads((ROOT/"dist/chignolin/data.json").read_text(encoding="utf-8"))["cartoons"]


def material(name, color):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color,1)
    m.use_nodes = True
    bs = m.node_tree.nodes.get("Principled BSDF")
    bs.inputs["Base Color"].default_value = (*color,1)
    bs.inputs["Roughness"].default_value = .3
    return m


def tube(points, radius, mat):
    curve = bpy.data.curves.new("Backbone", "CURVE")
    curve.dimensions = "3D"
    curve.bevel_depth = radius
    curve.bevel_resolution = 3
    s = curve.splines.new("POLY")
    s.points.add(len(points)-1)
    for a,p in zip(s.points,points):
        a.co = (*p,1)
    o = bpy.data.objects.new("Backbone",curve)
    bpy.context.collection.objects.link(o)
    o.data.materials.append(mat)


def render(name, coords, backbone, alanine=False):
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.use_gtao = True
    scene.eevee.taa_render_samples = 64
    scene.world.use_nodes = True
    scene.world.node_tree.nodes["Background"].inputs["Color"].default_value = (.015,.025,.04,1)
    scene.world.node_tree.nodes["Background"].inputs["Strength"].default_value = .7
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.exposure = -.6
    scene.render.resolution_x = 1000
    scene.render.resolution_y = 750
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    p = np.array(coords)
    p -= p.mean(0)
    # Face the principal molecular plane; preserve distances.
    _,_,vt = np.linalg.svd(p)
    p = p@vt.T
    path = p[backbone]
    colors = [material(f"Residue {i}",(.2+.7*i/(len(path)-1),.65,.9-.65*i/(len(path)-1)))
              for i in range(len(path))]
    if alanine:
        elements = ['C','C','O','N','C','C','C','O','N','C']
        mats = {e:material(e,c) for e,c in [('C',(.6,.75,.75)),('O',(.95,.25,.3)),('N',(.25,.4,.95))]}
        bonds = [[0,1],[1,2],[1,3],[3,4],[4,5],[4,6],[6,7],[6,8],[8,9]]
        for i,j in bonds:
            tube([p[i],p[j]],.014,mats['C'])
        for i,point in enumerate(p):
            bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,radius=.034,location=point)
            bpy.context.object.data.materials.append(mats[elements[i]])
    # Catmull-Rom interpolation passes through recorded backbone sites.
    padded = np.vstack([2*path[0]-path[1],path,2*path[-1]-path[-2]])
    smooth = []
    for i in range(len(path)-1):
        a,b,c,d = padded[i:i+4]
        for t in np.linspace(0,1,16,endpoint=False):
            smooth.append(.5*((2*b)+(-a+c)*t+(2*a-5*b+4*c-d)*t*t+(-a+3*b-3*c+d)*t**3))
    smooth = np.vstack([smooth,path[-1]])
    if alanine:
        for i in range(len(path)-1):
            tube(smooth[i*16:(i+1)*16+1],.019,colors[i])
    else:
        tangent = np.gradient(smooth,axis=0)
        tangent /= np.linalg.norm(tangent,axis=1)[:,None]
        side = np.cross(tangent,np.array([0,0,1]))
        side /= np.maximum(np.linalg.norm(side,axis=1)[:,None],1e-8)
        vertices = np.stack([smooth-side*.065,smooth+side*.065],axis=1).reshape(-1,3)
        faces = [(2*i,2*i+1,2*i+3,2*i+2) for i in range(len(smooth)-1)]
        mesh = bpy.data.meshes.new("CA ribbon")
        mesh.from_pydata(vertices.tolist(),[],faces);mesh.update()
        obj = bpy.data.objects.new("CA ribbon",mesh);bpy.context.collection.objects.link(obj)
        for mat in colors:
            obj.data.materials.append(mat)
        for i,poly in enumerate(mesh.polygons):
            poly.material_index = min(len(colors)-1,i//16);poly.use_smooth=True
        mod = obj.modifiers.new("Ribbon thickness","SOLIDIFY");mod.thickness=.015
    if not alanine:
        for i,point in enumerate(path):
            bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,radius=.035,location=point)
            bpy.context.object.data.materials.append(colors[i])
    bounds = np.vstack([p,smooth])
    center = (bounds.min(0)+bounds.max(0))/2
    bpy.ops.object.camera_add(location=center+np.array([0,0,8]))
    camera = bpy.context.object;scene.camera=camera;camera.data.type="ORTHO"
    camera.rotation_euler=(Vector(center)-camera.location).to_track_quat("-Z","Y").to_euler()
    camera.data.ortho_scale=max(np.ptp(bounds[:,0])*1.3,np.ptp(bounds[:,1])*1000/750*1.3)+.3
    for pos,power in [((1,1,4),70),((-2,-1,3),45)]:
        bpy.ops.object.light_add(type="AREA",location=pos)
        light=bpy.context.object;light.data.energy=power;light.data.size=3
    scene.render.filepath=str(OUT/(name+".png"))
    bpy.ops.render.render(write_still=True)


render("alanine-cartoon",alanine,[0,1,3,4,6,8,9],True)
render("chignolin-compact-cartoon",chig[0]["molecule"],list(range(10)))
render("chignolin-extended-cartoon",chig[1]["molecule"],list(range(10)))
