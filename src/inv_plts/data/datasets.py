from dataclasses import dataclass

import torch
from torch.utils.data import Dataset

class BasicInvasivePlantsDataset(Dataset):
    def __init__(self, transform=None):
        self.data = torch.rand(100, 3, 256, 256)
        self.labels = torch.randint(low=0, high=10, size=(self.data.shape[0],))
        self.transform = transform
        
    def __len__(self):
        return len(self.data)
    
    @dataclass
    class DataStructure:
        image: torch.Tensor
        label: int
    
    def __getitem__(self, idx) -> DataStructure:
        x = self.data[idx]
        y = self.labels[idx]
        if self.transform:
            x = self.transform(x)
            
        return BasicInvasivePlantsDataset.DataStructure(
            image = x,
            label = y
        )