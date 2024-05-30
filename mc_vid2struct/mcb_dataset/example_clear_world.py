import mcpi.minecraft as minecraft
from time import sleep
from tqdm import tqdm
from structure_building_utils import clear_world
from utils import get_pose
import sys

mc = minecraft.Minecraft.create()
base = (10, 1, 10)

size = int(sys.argv[1]) if len(sys.argv) > 1 else 50
clear_world(mc, base, n=size)