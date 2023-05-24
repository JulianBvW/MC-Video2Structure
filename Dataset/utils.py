def get_pose(mc):
    position_rel = mc.player.getPos()
    position_abs = position_rel.x+8, position_rel.y+4, position_rel.z+8
    rotation = mc.player.getRotation()
    pitch = mc.player.getPitch()

    pose = {
        'x': position_abs[0],
        'y': position_abs[1],
        'z': position_abs[2],
        'rot': rotation,
        'pit': pitch
    }

    return pose

SPAWN_OFFSET = ()