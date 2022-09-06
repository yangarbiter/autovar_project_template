"""Multi-layer perceptrons
"""
import torch.nn as nn
import torch.nn.functional as F


class MLP(nn.Module):
    """A basic MLP architecture."""

    def __init__(self, n_features, n_classes, n_channels=None):
        super(LargeMLP, self).__init__()
        self.hidden = nn.Linear(n_features[0], 256)
        self.hidden2 = nn.Linear(256, 256)
        self.hidden3 = nn.Linear(256, 256)
        self.fc = nn.Linear(256, n_classes)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = F.relu(self.hidden2(x))
        x = F.relu(self.hidden3(x))
        x = self.fc(x)
        return x

