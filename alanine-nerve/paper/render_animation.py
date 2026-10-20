"""Six-second Blender-rendered loop suitable for attaching to an exploratory post."""
import bpy, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
prefix="chignolin-" if "--chignolin" in sys.argv else ""
bpy.ops.wm.open_mainfile(filepath=str(root/("paper/"+prefix+"molecular-landscape.blend")))
s=bpy.context.scene
s.render.resolution_x=1280;s.render.resolution_y=840;s.render.resolution_percentage=100
s.render.fps=12;s.frame_start=1;s.frame_end=72
s.render.image_settings.file_format="FFMPEG"
s.render.ffmpeg.format="MPEG4";s.render.ffmpeg.codec="H264";s.render.ffmpeg.constant_rate_factor="HIGH"
s.render.filepath=str(root/("paper/figures/"+prefix+"deforming-landscape.mp4"))
objects=[o for o in s.objects if o.name.startswith("Route ") and o.data.shape_keys]
for frame in range(1,74):
    q=((frame-1)/72%1)*12;i=int(q);w=q-i
    for o in objects:
        keys=o.data.shape_keys.key_blocks
        for k,key in enumerate(list(keys)[1:]):
            key.value=(1-w if k==i else 0)+(w if k==(i+1)%12 else 0)
            key.keyframe_insert(data_path="value",frame=frame)
for o in objects:
    for curve in o.data.shape_keys.animation_data.action.fcurves:
        for point in curve.keyframe_points:point.interpolation="LINEAR"
bpy.ops.render.render(animation=True)
