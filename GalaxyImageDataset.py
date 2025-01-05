# import necessary packages and libaries
import torch
from torch.utils.data import Dataset, DataLoader
import torchvision
from torchvision.datasets import ImageFolder




# define class for image datset imported from Kaggle
class GalaxyImageDataset (Dataset) :
  def __init__(self, data_dir, transform=None):
        self.data = ImageFolder(data_dir, transform=transform)

  def __len__(self):
        return len(self.data)

  def __getitem__(self, idx):
        return self.data[idx]

  @property
  def classes(self):
        return self.data.classes



