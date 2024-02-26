from structure_building_utils import make_world
from utils import get_pose

import os
import sys
import pandas as pd
from tqdm import tqdm
from time import sleep
from datetime import datetime
import mcpi.minecraft as minecraft

out_dir = 'output/run_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
os.makedirs(out_dir)

mc = minecraft.Minecraft.create()
base = (10, 1, 10)

imgs_to_take = int(sys.argv[1]) if len(sys.argv) > 1 else 20
make_world(mc, base, n=4, it=10)

# Warum-Up Phase
for i in tqdm(range(50)):
    sleep(.1)
mc.postToChat('start')

# Get Poses
poses = []
for i in range(imgs_to_take):
    sleep(1)
    mc.postToChat(i)
    poses.append(get_pose(mc)) # Costs 0.15 Seconds -> FPS 6.6666
mc.postToChat('stop')

# Save Poses
poses = pd.DataFrame(poses)
poses.to_csv('out_dir/poses.csv')
print(poses)