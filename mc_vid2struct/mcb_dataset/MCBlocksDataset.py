from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import pandas as pd
import torch
import math

from mc_vid2struct.mcb_dataset.utils import rot_to_sin_cos_repr

CAMERA_SIZE = (854 // 2, 480 // 2) # (854, 480)
DEFAULT_TRANSFORM = transforms.Compose([
    transforms.Resize(CAMERA_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.3955, 0.3832, 0.3661], std=[0.1625, 0.1902, 0.2550])
])

class MCBlocksDataset(Dataset):
    def __init__(self, dataset_path='mc_vid2struct/mcb_dataset/dataset/', transform=DEFAULT_TRANSFORM):
        self.screenshot_path = dataset_path + 'screenshots/'
        self.poses = pd.read_csv(dataset_path + 'poses.csv')
        self.transform = transform
    
    def __len__(self):
        return len(self.poses)

    def __getitem__(self, idx):

        # Normal Screenshot
        screenshot = Image.open(self.screenshot_path + str(idx) + '.png').convert('RGB')
        screenshot = self.transform(screenshot)

        # TODO pitch
        pit = self.poses['pit'][idx]
        labels = torch.tensor(rot_to_sin_cos_repr(pit), dtype=torch.float)

        # TODO y level
        # y_level = self.poses['y'][idx] - math.floor(self.poses['y'][idx]) # TODO only get local coord

        return screenshot, labels
