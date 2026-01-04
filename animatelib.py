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


def collide(
    obj_a: bpy.types.Object,
    obj_b: bpy.types.Object,
    mass_a: float,
    mass_b: float,
    collision_coords_a: tuple[float, float, float],
    collision_coords_b: tuple[float, float, float],
    start_frame: int,
    collision_frame: int,
    end_frame: int,
    distance: tuple[float, float, float],
):
    start_coords_a = (
        collision_coords_a[0] + distance[0],
        collision_coords_a[1] + distance[1],
        collision_coords_a[2] + distance[2],
    )

    # calculate velocity of A at collision (derivative of t^5 easing at t=1 is 5)
    frames_before_collision = collision_frame - start_frame
    distance_magnitude = (distance[0] ** 2 + distance[1] ** 2 + distance[2] ** 2) ** 0.5
    velocity_a_at_collision = 5 * distance_magnitude / frames_before_collision

    # momentum conservation: v_combined = (m_a * v_a) / (m_a + m_b)
    velocity_combined = (mass_a * velocity_a_at_collision) / (mass_a + mass_b)

    # direction of travel (normalized distance vector, inverted since A moves toward collision)
    direction = (
        -distance[0] / distance_magnitude,
        -distance[1] / distance_magnitude,
        -distance[2] / distance_magnitude,
    )

    # how far do they travel after collision while decelerating linearly to stop?
    # linear decel: average velocity is half of initial, distance = v_avg * time
    frames_after_collision = end_frame - collision_frame
    post_collision_distance = velocity_combined * frames_after_collision / 2

    end_coords_a = (
        collision_coords_a[0] + direction[0] * post_collision_distance,
        collision_coords_a[1] + direction[1] * post_collision_distance,
        collision_coords_a[2] + direction[2] * post_collision_distance,
    )
    end_coords_b = (
        collision_coords_b[0] + direction[0] * post_collision_distance,
        collision_coords_b[1] + direction[1] * post_collision_distance,
        collision_coords_b[2] + direction[2] * post_collision_distance,
    )

    # animate A: ease-in from start to collision
    for frame in range(start_frame, collision_frame + 1):
        loc = get_location(
            start_coords_a, collision_coords_a, start_frame, frame, collision_frame
        )
        obj_a.location.x = loc[0]
        obj_a.location.y = loc[1]
        obj_a.location.z = loc[2]
        obj_a.keyframe_insert(data_path="location", frame=frame)

    # animate B: stationary until collision
    obj_b.location.x = collision_coords_b[0]
    obj_b.location.y = collision_coords_b[1]
    obj_b.location.z = collision_coords_b[2]
    obj_b.keyframe_insert(data_path="location", frame=start_frame)
    obj_b.keyframe_insert(data_path="location", frame=collision_frame)

    # animate both: linear deceleration from collision to end
    for frame in range(collision_frame + 1, end_frame + 1):
        t = (frame - collision_frame) / frames_after_collision
        # linear decel: position follows t * (2 - t) curve (integral of linear velocity decay)
        ease = t * (2 - t)

        loc_a = (
            collision_coords_a[0] + (end_coords_a[0] - collision_coords_a[0]) * ease,
            collision_coords_a[1] + (end_coords_a[1] - collision_coords_a[1]) * ease,
            collision_coords_a[2] + (end_coords_a[2] - collision_coords_a[2]) * ease,
        )
        obj_a.location.x = loc_a[0]
        obj_a.location.y = loc_a[1]
        obj_a.location.z = loc_a[2]
        obj_a.keyframe_insert(data_path="location", frame=frame)

        loc_b = (
            collision_coords_b[0] + (end_coords_b[0] - collision_coords_b[0]) * ease,
            collision_coords_b[1] + (end_coords_b[1] - collision_coords_b[1]) * ease,
            collision_coords_b[2] + (end_coords_b[2] - collision_coords_b[2]) * ease,
        )
        obj_b.location.x = loc_b[0]
        obj_b.location.y = loc_b[1]
        obj_b.location.z = loc_b[2]
        obj_b.keyframe_insert(data_path="location", frame=frame)
