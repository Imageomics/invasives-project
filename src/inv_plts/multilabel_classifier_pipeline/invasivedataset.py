# Setup identification dataset

import torch
from torch import nn
from pathlib import Path
import pandas as pd 
import json
import matplotlib.pyplot as plt 
import numpy as np
import os
import torch.nn.functional as F
from tqdm import tqdm

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

class BasicInvasivePlantsDataset(Dataset):
    def __init__(
            self, 
            data_file:Path,
            img_dir:Path,
            transform,
            traits_to_detect = ["Healthy", "Leaf Miner?", "Rust?", "Other Insect? (catipillar bites, etc.)", "Mechanical? (human, animal, herbicide, etc.)"]
        ):
        
        self.df = pd.read_csv(data_file)
        
        self.image_root = img_dir
        self.df = self.df.fillna("NA")
        self.transform = transform
        self.traits_to_detect = traits_to_detect
    
    def _get_image_path(self, session_folder, fname):
        img_path = self.image_root / f"{session_folder}/{fname}"
        return img_path
    
    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, idx):
        idx = int(idx)
        row = self.df.iloc[idx]

        # Image
        fname = row["Original\nFilename"]
        session_folder = row["Session\nFolder Name"]
        img_path = self._get_image_path(session_folder=session_folder, fname=fname)
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
        labels = [
            is_healthy,
            leaf_miner_damage,
            rust_damage,
            other_insect_damage,
            mechanical_damage,
        ]

        labels = [float(l) for l in labels]
        labels = np.array(labels)

        return img, labels