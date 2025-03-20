import torchvision.transforms as T

from pathlib import Path
from inv_plts.data.datasets import BasicInvasivePlantsDataset


def test_basic_dataset():
    image_root_path = Path("/local/scratch/carlyn.1/invasive-image-sessions")
    metadata_csv = Path("tmp/metadata/linked_metadata.csv")

    transforms = T.Compose(
        [
            T.Resize((224, 224)),
            T.ToTensor(),
            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    dataset = BasicInvasivePlantsDataset(
        image_root=image_root_path, metadata_csv=metadata_csv, transform=transforms
    )
    data: BasicInvasivePlantsDataset.DataStructure
    for data in dataset:
        print(data.image.shape)
        print(data.label.shape)
        data.image + 10
        data.label - 5


if __name__ == "__main__":
    test_basic_dataset()
