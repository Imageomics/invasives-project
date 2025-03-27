import torch
from torch.optim import SGD
from torch.nn import CrossEntropyLoss

from inv_plts.data.datasets import BasicDataset
from inv_plts.models.simple import BasicCNN

def test_basic_cnn_forward():
    net = BasicCNN()
    
    dataset = BasicDataset()
    data: BasicDataset.DataStructure
    
    for data in dataset:
        out = net(data.image.unsqueeze(0))

def test_basic_cnn_train():
    net = BasicCNN()
    
    dataset = BasicDataset()
    data: BasicDataset.DataStructure
    
    optimizer = SGD(net.parameters(), lr=0.001)
    cel_fn = CrossEntropyLoss()
    for data in dataset:
        optimizer.zero_grad()
        out = net(data.image.unsqueeze(0))
        loss = cel_fn(out, torch.tensor([data.label]))
        loss.backward()
        optimizer.step()