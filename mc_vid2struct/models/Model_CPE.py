# Model to estimate the Camera Pose from the MC Blocks Dataset

import torch.nn.functional as F
import torch.nn as nn
import numpy as np

from mc_vid2struct.models.utils import conv_output_shape
from mc_vid2struct.mcb_dataset.MCBlocksDataset import CAMERA_SIZE

class Model_CPE(nn.Module):
    def __init__(self):
        super(Model_CPE, self).__init__()
        self.camera_size = CAMERA_SIZE
        self.final_conv_channels = 64
        
        # Convolutional layers
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=self.final_conv_channels, kernel_size=3, stride=1, padding=1)

        # Pooling layer
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)

        # Size after convolutional layers and pooling
        self.size_after_convs = self.camera_size
        self.size_after_convs = conv_output_shape(self.size_after_convs, kernel_size=3, stride=1, pad=1, max_pool=2)
        self.size_after_convs = conv_output_shape(self.size_after_convs, kernel_size=3, stride=1, pad=1, max_pool=2)
        self.size_after_convs = conv_output_shape(self.size_after_convs, kernel_size=3, stride=1, pad=1, max_pool=2)
        self.fc_input_size = np.prod(self.size_after_convs) * self.final_conv_channels
        
        # Fully connected layers
        self.fc1 = nn.Linear(in_features=self.fc_input_size, out_features=512*2)
        self.fc2 = nn.Linear(in_features=512*2, out_features=128)
        self.fc3 = nn.Linear(in_features=128, out_features=2)
    
    def forward(self, x):

        # Convolutional and pooling layers
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        
        # Flatten the tensor
        x = x.view(-1, self.fc_input_size)
        
        # Fully connected layers
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x