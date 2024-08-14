import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split

from tqdm import tqdm
from datetime import datetime

from mc_vid2struct.mcb_dataset.MCBlocksDataset import MCBlocksDataset
from mc_vid2struct.training.circular_loss import CircularLoss
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

criterion = CircularLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

### Train loop

NUM_EPOCHS = 50 # TODO ArgParse

start_time = datetime.now()
for epoch in range(NUM_EPOCHS):
    model.train()
    running_loss = 0.0

    for screenshots, labels in tqdm(train_loader):
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

print('Finished training after:', datetime.now() - start_time)

model.eval()
test_loss = 0.0

with torch.no_grad():
    for screenshots, labels in tqdm(test_loader):
        screenshots, labels = screenshots.to(DEVICE), labels.to(DEVICE)
        outputs = model(screenshots)
        loss = criterion(outputs, labels.view((-1, 1)))
        for i in range(len(labels)):
            print(outputs[i], labels.view((-1, 1))[i])
        test_loss += loss.item() * screenshots.size(0)
        screenshots, labels = screenshots.to('cpu'), labels.to('cpu')

test_loss /= len(test_loader.dataset)
print(f'Test Loss: {test_loss:.4f}')