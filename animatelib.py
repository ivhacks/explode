import bpy

FPS = 240


def seconds_to_frames(seconds: float) -> int:
    return round(seconds * FPS)


def get_location(
    start_location: tuple[float, float, float],
    end_location: tuple[float, float, float],
    start_frame: int,
    current_frame: int,
    end_frame: int,
) -> tuple[float, float, float]:
    if current_frame <= start_frame:
        return start_location
    if current_frame >= end_frame:
        return end_location

    t = (current_frame - start_frame) / (end_frame - start_frame)
    ease = t**5

    return (
        start_location[0] + (end_location[0] - start_location[0]) * ease,
        start_location[1] + (end_location[1] - start_location[1]) * ease,
        start_location[2] + (end_location[2] - start_location[2]) * ease,
    )


def animate_assemble(
    obj: bpy.types.Object,
    end_frame: int,
    length: float,
    distance: tuple[float, float, float],
):
    end_location = (obj.location.x, obj.location.y, obj.location.z)
    start_location = (
        end_location[0] + distance[0],
        end_location[1] + distance[1],
        end_location[2] + distance[2],
    )
    start_frame = end_frame - seconds_to_frames(length)

    for frame in range(start_frame, end_frame + 1):
        loc = get_location(start_location, end_location, start_frame, frame, end_frame)
        obj.location.x = loc[0]
        obj.location.y = loc[1]
        obj.location.z = loc[2]
        obj.keyframe_insert(data_path="location", frame=frame)
