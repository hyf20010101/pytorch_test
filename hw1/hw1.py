from sqlalchemy import true
import torch
from torch.utils.data import DataLoader, Dataset


class myDataSet(Dataset):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return super().__getitem__(index)


DataFile = open('/Users/michael/test.txt', 'r')
dataset = myDataSet(DataFile)
dataloader = DataLoader(dataset, batch_size=1, shuffle=true)
