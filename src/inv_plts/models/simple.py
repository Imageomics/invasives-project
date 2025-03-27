import torch
import torch.nn as nn


class BasicCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 16, kernel_size=3)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(in_features=64, out_features=10, bias=True)

    def forward(self, x):
        h = self.relu(self.conv(x))
        h = self.relu(self.conv2(h))
        h = self.relu(self.conv3(h))
        feats = torch.flatten(self.avgpool(h), start_dim=1)
        return self.fc(feats)


class BasicInvasiveSpeciesCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 16, kernel_size=3)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(in_features=64, out_features=5, bias=True)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.conv(x))
        h = self.relu(self.conv2(h))
        h = self.relu(self.conv3(h))
        feats = torch.flatten(self.avgpool(h), start_dim=1)
        out = self.sigmoid(self.fc(feats))
        return out
