import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from tqdm import tqdm

from mc_vid2struct.mcb_dataset.MCBlocksDataset import MCBlocksDataset
from mc_vid2struct.models.Model_CPE import Model_CPE


DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu') # TODO argparse

### Load Dataset

full_dataset = MCBlocksDataset()
train_dataset, test_dataset = random_split(full_dataset, [0.8, 0.2])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=4)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, num_workers=4)

### Load Model

model = Model_CPE().to(DEVICE)

### Load Loss and Optimizer

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

### Train loop

NUM_EPOCHS = 10 # TODO ArgParse
for epoch in tqdm(range(NUM_EPOCHS)):
    model.train()
    running_loss = 0.0

    for screenshots, labels in train_loader:
        screenshots, labels = screenshots.to(DEVICE), labels.to(DEVICE)

        optimizer.zero_grad()
        outputs = model(screenshots)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * screenshots.size(0)
        screenshots, labels = screenshots.to('cpu'), labels.to('cpu')
    
    epoch_loss = running_loss / len(train_loader.dataset)
    print(f'Epoch {epoch+1}/{NUM_EPOCHS}, Loss: {epoch_loss:.4f}')