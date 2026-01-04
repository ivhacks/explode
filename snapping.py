import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import bpy

from animatelib import collide

cube0 = bpy.data.objects["Cube0"]
cube1 = bpy.data.objects["Cube1"]

collide(
    obj_a=cube1,
    obj_b=cube0,
    mass_a=1.0,
    mass_b=8.0,
    collision_coords_a=(0.0, 1.5, 0.0),
    collision_coords_b=(0.0, 0.0, 0.0),
    start_frame=0,
    collision_frame=240,
    end_frame=480,
    distance=(0.0, 5.0, 0.0),
)

bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
