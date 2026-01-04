import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import bpy

from animatelib import animate_assemble

cube0 = bpy.data.objects["Cube0"]
cube1 = bpy.data.objects["Cube1"]

animate_assemble(cube1, 240, 1, (0.0, 5.0, 0.0))

bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
