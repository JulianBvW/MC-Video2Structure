# Converts the multiple output folders of the data creation runs to one dataset folder

import os
import sys
import shutil
import pandas as pd

dataset_folder = 'dataset/'
data_folder = 'output/'

shutil.rmtree(dataset_folder, ignore_errors=True)
os.makedirs(dataset_folder)
os.makedirs(dataset_folder + 'screenshots/')

# Get all runs

run_folders = sorted(os.listdir(data_folder))

### Poses

pose_dfs = []
for dir in run_folders:
    pose_dfs.append(pd.read_csv(data_folder + dir + '/poses.csv'))
poses = pd.concat(pose_dfs, ignore_index=True)
poses.to_csv(dataset_folder + 'poses.csv', index=False)

### Normal Screenshots

i = 0
for dir in run_folders:
    screenshots = sorted(os.listdir(data_folder + dir + '/screenshots/'))
    for img_idx in range(len(screenshots)):
        shutil.copy(data_folder + dir + '/screenshots/' + str(img_idx) + '.png', dataset_folder + 'screenshots/' + str(i) + '.png')
        i += 1

### BSA Data

# TBA

### BDE Data

# TBA