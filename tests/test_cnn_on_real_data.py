from pathlib import Path
from tqdm.auto import tqdm

from torch.optim import SGD
from torch.nn import BCELoss
import torchvision.transforms as T

from inv_plts.data.datasets import BasicInvasivePlantsDataset
from inv_plts.models.simple import BasicInvasiveSpeciesCNN


def test_basic_cnn():
    net = BasicInvasiveSpeciesCNN()

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
    optimizer = SGD(net.parameters(), lr=0.001)
    loss_fn = BCELoss()
    tbar = tqdm(range(10), desc="Training")
    for idx in tbar:
        data = dataset[idx]
        optimizer.zero_grad()
        out = net(data.image.unsqueeze(0))
        loss = loss_fn(out, data.label.unsqueeze(0))
        loss.backward()
        optimizer.step()

        tbar.set_postfix({"loss": loss.item()})
        tbar.refresh()


if __name__ == "__main__":
    test_basic_cnn()
