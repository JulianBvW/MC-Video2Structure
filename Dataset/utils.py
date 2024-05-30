import math

def get_pose(mc):
    position_rel = mc.player.getPos()
    position_abs = position_rel.x-SPAWN_OFFSET[0], position_rel.y-SPAWN_OFFSET[1], position_rel.z-SPAWN_OFFSET[2]
    rotation = mc.player.getRotation()
    rotation *= -1 if list(mc.player.getDirection())[0] > 0 else 1
    pitch = mc.player.getPitch()

    pose = {
        'x': position_abs[0],
        'y': position_abs[1],
        'z': position_abs[2],
        'rot': rotation,
        'pit': pitch
    }

    return pose

SPAWN_OFFSET = (-8, -4, -8)

def rot_to_sin_cos_repr(rot):
    rot += 180
    rot %= 90
    rot *= 4
    rot = math.radians(rot)
    return math.sin(rot), math.cos(rot)

def sin_cos_repr_to_rot(sin_value, cos_value):
    rot = math.atan2(sin_value, cos_value)
    rot = math.degrees(rot)
    rot /= 4
    rot += 90 if rot < 0 else 0
    return rot
