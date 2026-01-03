import bpy


def animate_assemble(obj: bpy.types.Object, end_frame: int):
    original_z = obj.location.z

    bpy.context.scene.frame_set(end_frame - 60)
    obj.location.z = original_z + 1.0
    obj.keyframe_insert(data_path="location", frame=end_frame - 60)

    bpy.context.scene.frame_set(end_frame)
    obj.location.z = original_z
    obj.keyframe_insert(data_path="location", frame=end_frame)


cube0 = bpy.data.objects["Cube0"]
cube1 = bpy.data.objects["Cube1"]
cube2 = bpy.data.objects["Cube2"]

animate_assemble(cube0, 100)
animate_assemble(cube1, 140)
animate_assemble(cube2, 180)

bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
