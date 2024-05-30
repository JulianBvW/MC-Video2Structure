import torch.utils
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms
from PIL import Image
import pandas as pd
import math

DEFAULT_TRANSFORM = transforms.Compose([
    transforms.Resize((854 // 2, 480 // 2)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.3955, 0.3832, 0.3661], std=[0.1625, 0.1902, 0.2550])
])

class MCBlockDataset(Dataset):
    def __init__(self, dataset_path='Dataset/dataset/', transform=DEFAULT_TRANSFORM):
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

        # TODO y level
        # y_level = self.poses['y'][idx] - math.floor(self.poses['y'][idx]) # TODO only get local coord

        return screenshot, pit

full_dataset = MCBlockDataset()
train_dataset, test_dataset = random_split(full_dataset, [0.8, 0.2])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=4)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, num_workers=4)
