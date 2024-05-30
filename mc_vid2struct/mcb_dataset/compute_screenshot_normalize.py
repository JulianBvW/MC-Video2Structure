# Computes the `mean` and `std` for the screenshots of the dataset for the `transforms.Normalize()` transformation

import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from tqdm import tqdm

from mc_vid2struct.mcb_dataset.MCBlocksDataset import MCBlocksDataset

NO_NORM_TRANSFORM = transforms.Compose([
    transforms.Resize((854 // 2, 480 // 2)),
    transforms.ToTensor()
])

# Load the dataset
dataset = MCBlocksDataset(transform=NO_NORM_TRANSFORM)
dataloader = DataLoader(dataset, batch_size=64, shuffle=False, num_workers=4)

# Initialize normalization variables
mean = torch.zeros(3)
std = torch.zeros(3)
n = 0

for screenshots, _ in tqdm(dataloader):
    batch_size = screenshots.size(0)
    channels = screenshots.size(1)
    screenshots = screenshots.view(batch_size, channels, -1)  # Reshape images to (batch_size, channels, height*width)
    mean += screenshots.mean(2).sum(0)  # Sum the mean of each channel
    std += screenshots.std(2).sum(0)  # Sum the standard deviation of each channel
    n += batch_size  # Keep track of the number of screenshots

# Calculate the mean and std
mean /= n
std /= n

print(f'Mean: {mean}')
print(f'Std: {std}')