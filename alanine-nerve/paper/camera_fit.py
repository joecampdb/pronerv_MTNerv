"""Frame all mesh/curve bounds in an orthographic camera, including thin overlays."""
import bpy
from mathutils import Vector
def fit_camera(scene,padding=1.15):
 bpy.context.view_layer.update()
 points=[o.matrix_world@Vector(corner) for o in scene.objects if o.type in {'MESH','CURVE'} and not o.hide_render for corner in o.bound_box]
 camera=scene.camera;rotation=camera.rotation_euler.to_matrix();inv=rotation.transposed()
 local=[inv@p for p in points]
 low=Vector(tuple(min(p[k] for p in local) for k in range(3)));high=Vector(tuple(max(p[k] for p in local) for k in range(3)))
 center=rotation@((low+high)*.5)
 camera.location=center+rotation@Vector((0,0,60))
 camera.data.ortho_scale=max(high.x-low.x,(high.y-low.y)*scene.render.resolution_x/scene.render.resolution_y)*padding
 camera.data.clip_end=300
