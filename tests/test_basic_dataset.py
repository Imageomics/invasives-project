from inv_plts.data.datasets import BasicInvasivePlantsDataset

def test_basic_dataset():
    dataset = BasicInvasivePlantsDataset()
    data: BasicInvasivePlantsDataset.DataStructure
    for data in dataset:
        data.image + 10
        data.label - 5

