from inv_plts.data.datasets import BasicDataset

def test_basic_dataset():
    dataset = BasicDataset()
    data: BasicDataset.DataStructure
    for data in dataset:
        data.image + 10
        data.label - 5

