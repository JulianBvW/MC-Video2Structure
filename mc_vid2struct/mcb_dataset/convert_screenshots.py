# Converts the three sets of screenshots (normal, BSA, BDE) for the MC Blocks dataset

import os
import sys

folder = 'output/' + sys.argv[1]

### Normal Screenshots

screenshots = sorted(os.listdir(folder + '/screenshots/'))
for i, img in enumerate(screenshots):
    os.rename(folder + '/screenshots/' + img, folder + '/screenshots/' + str(i) + '.png')

### BSA Screenshots

# TBA

### BDE Screenshots

# TBA