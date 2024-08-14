import torch
import torch.nn as nn
import torch.nn.functional as F

class CircularLoss(nn.Module):
    def __init__(self):
        super(CircularLoss, self).__init__()
        self.mse_loss = nn.MSELoss()
    
    def forward(self, outputs, targets):
        pit_sin_pred, pit_cos_pred = outputs[:, 0], outputs[:, 1]
        pit_sin_true, pit_cos_true = targets[:, 0], targets[:, 1]
        
        loss_pit_sin = self.mse_loss(pit_sin_pred, pit_sin_true)
        loss_pit_cos = self.mse_loss(pit_cos_pred, pit_cos_true)
        
        return loss_pit_sin + loss_pit_cos