import bpy

FPS = 240


def seconds_to_frames(seconds: float) -> int:
    return round(seconds * FPS)


def animate_assemble(
    obj: bpy.types.Object, end_frame: int, length: float, distance: float
):
    original_z = obj.location.z
    start_frame = end_frame - seconds_to_frames(length)

    bpy.context.scene.frame_set(start_frame)
    obj.location.z = original_z + distance
    obj.keyframe_insert(data_path="location", frame=start_frame)

    bpy.context.scene.frame_set(end_frame)
    obj.location.z = original_z
    obj.keyframe_insert(data_path="location", frame=end_frame)

    action = obj.animation_data.action
    fcurves = action.layers[0].strips[0].channelbags[0].fcurves
    for fcurve in fcurves:
        if fcurve.data_path == "location":
            for keyframe in fcurve.keyframe_points:
                if keyframe.co[0] == start_frame:
                    keyframe.interpolation = "QUINT"
                    keyframe.easing = "EASE_IN"
