import mcpi.minecraft as minecraft
from time import sleep
from tqdm import tqdm
from structure_building_utils import make_world
from utils import get_pose
import sys

mc = minecraft.Minecraft.create()
base = (10, 1, 10)

size = int(sys.argv[1]) if len(sys.argv) > 1 else 3
make_world(mc, base, n=size, it=((size+1)//2)**2)

# for i in tqdm(range(50)):
#     sleep(.1)

# poses = []

# from datetime import datetime
# now = datetime.now()
# poses.append((0, get_pose(mc)))
# print(datetime.now() - now)
# for i in range(60):
#     poses.append((i, get_pose(mc))) # Costs 0.15 Seconds -> FPS 6.6666

# print(datetime.now() - now)
# poses.append((30, get_pose(mc)))
# print(datetime.now() - now)
# for i in range(100):
#     sleep(1/30)
#     mc.postToChat(i)

# mc.postToChat('stop')

# for pose in poses:
#     print(pose)