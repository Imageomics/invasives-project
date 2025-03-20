from dataclasses import dataclass

import pandas as pd
import torch
from torch.utils.data import Dataset
from PIL import Image


class BasicDataset(Dataset):
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

        return BasicDataset.DataStructure(image=x, label=y)


class BasicInvasivePlantsDataset(Dataset):
    def __init__(self, image_root, metadata_csv, transform=None):
        self.image_root = image_root
        self.df = pd.read_csv(metadata_csv)
        self.df = self.df.fillna("NA")
        self.transform = transform

    def __len__(self):
        return self.df.shape[0]

    @dataclass
    class DataStructure:
        image: torch.Tensor
        label: int

    def __getitem__(self, idx) -> DataStructure:
        row = self.df.iloc[idx]

        # Image
        fname = row["Original\nFilename"]
        session_folder = row["Session\nFolder Name"]
        img_path = self.image_root / f"{session_folder}/{fname}"
        img = Image.open(img_path)
        if self.transform:
            img = self.transform(img)

        # Labels
        is_healthy = row["Healthy"].lower().strip() == "yes"
        leaf_miner_damage = row["Leaf Miner?"].lower().strip() == "yes"
        rust_damage = row["Rust?"].lower().strip() == "yes"
        other_insect_damage = (
            row["Other Insect? (catipillar bites, etc.)"].lower().strip() == "yes"
        )
        mechanical_damage = (
            row["Mechanical? (human, animal, herbicide, etc.)"].lower().strip() == "yes"
        )
        labels = torch.tensor(
            [
                is_healthy,
                leaf_miner_damage,
                rust_damage,
                other_insect_damage,
                mechanical_damage,
            ]
        ).type(torch.FloatTensor)

        return BasicInvasivePlantsDataset.DataStructure(image=img, label=labels)
