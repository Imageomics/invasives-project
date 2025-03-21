from dataclasses import dataclass
from pathlib import Path

from tqdm.auto import tqdm
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
        self.preprocess_dir = None

    def preprocess(self, preprocess_dir):
        preprocess_dir = Path(preprocess_dir)
        preprocess_dir.mkdir(parents=True, exist_ok=True)
        for i in tqdm(
            range(self.df.shape[0]), desc="Preprocessing Dataset", colour="#5AC433"
        ):
            row = self.df.iloc[i]
            fname = row["Original\nFilename"]
            session_folder = row["Session\nFolder Name"]
            img_path = self._get_image_path(session_folder=session_folder, fname=fname)
            img = Image.open(img_path)
            new_image_path = preprocess_dir / f"{session_folder}/{fname}"
            new_image_path.parent.mkdir(parents=True, exist_ok=True)
            if img.size[0] > 512 or img.size[1] > 512:
                img = img.resize((512, 512))
            img.save(new_image_path)

        self.preprocess_dir = preprocess_dir

    def _get_image_path(self, session_folder, fname):
        if self.preprocess_dir is None:
            img_path = self.image_root / f"{session_folder}/{fname}"
        else:
            img_path = self.preprocess_dir / f"{session_folder}/{fname}"
        return img_path

    @dataclass
    class DataStructure:
        image: torch.Tensor
        label: int

    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, idx) -> DataStructure:
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
