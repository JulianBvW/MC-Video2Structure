import structure_field_creator
from blocklist import id2mcpi
import numpy as np

def place_structure(mc, base, structure):
    bX, bY, bZ = base
    structure = np.rot90(structure)

    for x in range(len(structure)):
        for y in range(len(structure[x])):
            for z in range(len(structure[x][y])):
                block = id2mcpi[structure[x][y][z]]
                mc.setBlock(bX+x, bY+y, bZ+z, block)

def place_field(mc, base, structure_list):
    bX, bY, bZ = base
    for (offsetX, offsetY, offsetZ), structure in structure_list:
        place_structure(mc, (bX+offsetX, bY+offsetY, bZ+offsetZ), structure)

def clear_world(mc, base, n=50):
    bX, bY, bZ = base
    mc.setBlocks(bX, bY, bZ, bX+50, bY+50, bZ+50, 0)

def make_world(mc, base, n=3, it=5):
    clear_world(mc, base)
    FIELD = structure_field_creator.generate_structure_field(n=n, it=it)
    place_field(mc, base, FIELD)

