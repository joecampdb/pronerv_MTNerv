"""Re-frame existing measured scenes without regenerating scientific geometry."""
import bpy,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from camera_fit import fit_camera
for name in ['alanine','chignolin']:
 path=ROOT/f'output/measured-scenes/{name}.blend';bpy.ops.wm.open_mainfile(filepath=str(path));s=bpy.context.scene
 prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='OPTIX';prefs.get_devices()
 for device in prefs.devices:device.use=device.type=='OPTIX'
 s.cycles.device='GPU';fit_camera(s)
 bpy.ops.wm.save_as_mainfile(filepath=str(path));bpy.ops.render.render(write_still=True)
