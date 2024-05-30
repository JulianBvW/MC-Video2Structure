from blocklist import k2id, place_holder_building_2_idlist, place_holder_decoration_2_idlist
import numpy as np
import os

STRUC_DIR = 'structurefiles/'

GARDEN = [STRUC_DIR + f for f in os.listdir(STRUC_DIR) if f.startswith('garden')]
BASE   = [STRUC_DIR + f for f in os.listdir(STRUC_DIR) if f.startswith('base')]
ROOF   = [STRUC_DIR + f for f in os.listdir(STRUC_DIR) if f.startswith('roof')]
ALL    = [STRUC_DIR + f for f in os.listdir(STRUC_DIR)]

EXTRA_OFFSET = 5

def parse_line(line, random_textures):
    blocks = []
    for block in line:
        if block in random_textures:
            blocks.append(random_textures[block])
        elif block in place_holder_decoration_2_idlist:
            blocks.append(np.random.choice(place_holder_decoration_2_idlist[block]))
        else:
            blocks.append(k2id[block])
    return blocks

def parse_layers(lines, random_textures):
    layers = []
    current_layer = []
    for line in lines:
        if line == '\n':
            layers.append(current_layer)
            current_layer = []
        else:
            blocks = parse_line(line[:-1], random_textures)
            current_layer.append(blocks)
    layers.append(current_layer)
    return layers

def read_structure(fname, rotate=True):
    with open(fname) as f:
        lines = f.readlines()
    
    # Get random textures for building blocks
    random_textures = {
        'F': np.random.choice(place_holder_building_2_idlist['F']), # Foundation
        'S': np.random.choice(place_holder_building_2_idlist['S']), # Support
        'W': np.random.choice(place_holder_building_2_idlist['W']), # Wall
        'R': np.random.choice(place_holder_building_2_idlist['R'])  # Roof
    }
        
    structure = np.array(parse_layers(lines, random_textures))

    if rotate:
        struc_list = []
        times = np.random.choice([0, 1, 2, 3])
        for i in range(len(structure)):
            struc_list.append(np.rot90(structure[i], k=times))
        structure = np.array(struc_list)

    return structure

def read_random(type=None, rotate=True):
    if type == 'base':
        return read_structure(np.random.choice(BASE), rotate=rotate)
    if type == 'garden':
        return read_structure(np.random.choice(GARDEN), rotate=rotate)
    if type == 'roof':
        return read_structure(np.random.choice(ROOF), rotate=rotate)
    return read_structure(np.random.choice(ALL), rotate=rotate)

def generate_heights(n=3, it=9):
    heights = np.zeros((n, n))
    for _ in range(it):
        heights[np.random.choice(range(n))][np.random.choice(range(n))] += 1
    return heights

def generate_structure_field(n=3, it=9):
    heights = generate_heights(n=n, it=it)
    structures = []
    offsetX = 0
    for x in range(len(heights)):
        offsetZ = 0
        for z in range(len(heights[x])):
            offsetY = 0
            height = int(heights[x][z])
            if height == 0:
                build = ((offsetX, offsetY, offsetZ), read_random(type='garden'))
                structures.append(build)
            else:
                for _ in range(height):
                    build = ((offsetX, offsetY, offsetZ), read_random(type='base'))
                    structures.append(build)
                    offsetY += EXTRA_OFFSET
                build = ((offsetX, offsetY, offsetZ), read_random(type='roof'))
                structures.append(build)
            offsetZ += EXTRA_OFFSET
        offsetX += EXTRA_OFFSET
    return structures
