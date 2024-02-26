'''
List of blocks and ids.
'''

# Mapping of block names to ids
b2id = {
    'air': 0,
    'stone': 1,
    'cobblestone': 2,
    'slabs': 3,
    'bricks': 4,
    'grass': 5,
    'dirt': 6,
    'sand': 7,
    'planks': 8,
    'log': 9,
    'leaves': 10,
    'wool': 11,
    'goldblock': 12,
    'ironblock': 13,
    'diamondblock': 14,
    'bookshelf': 15,
    'obsidian': 16,
    'glowstone': 17,
    'melon': 18
}

# Mapping of structure file symbols (keys) to ids
k2id = {
    ' ': 0,    # air
    's': 1,    # stone
    'c': 2,    # cobblestone
    'b': 3,    # slabs (retextured crafting table)
    'X': 4,    # bricks
    'D': 5,    # grass
    'd': 6,    # dirt
    '~': 7,    # sand
    'w': 8,    # planks
    'L': 9,    # log
    'l': 10,   # leaves
    '%': 11,   # wool
    '-': 12,   # goldblock
    '=': 13,   # ironblock
    '+': 14,   # diamondblock
    '*': 15,   # bookshelf
    'O': 16,   # obsidian
    'G': 17,   # glowstone
    '@': 18    # melon
}

# Mapping of structure file *building* place holders to list of possible block ids
# These are random for every 5x5 structure
place_holder_building_2_idlist = {
    'F': [1, 2, 3, 4, 8, 11], # Foundation
    'S': [9, 9, 9, 2, 3, 4],  # Support
    'W': [1, 2, 4, 8, 11],    # Wall
    'R': [2, 4, 8, 8, 8]      # Roof
}

# Mapping of structure file *decoration* place holders to list of possible block ids
# These are random for every block
place_holder_decoration_2_idlist = {
    '$': [0, 0, 0, 0, 0, 0, 12, 13, 14, 15, 15, 15, 17, 17], # Interior
    '#': [0, 0, 0, 5, 5, 10, 15, 18, 18, 18]                 # Garden
}

# Mapping of ids to mcpi_ids
id2mcpi = {
    0:  0,
    1:  1,
    2:  4,
    3:  58, # (retextured crafting table)
    4:  45,
    5:  2,
    6:  3,
    7:  12,
    8:  5,
    9:  17,
    10: 18,
    11: 35,
    12: 41,
    13: 42,
    14: 57,
    15: 47,
    16: 49,
    17: 89,
    18: 103
}