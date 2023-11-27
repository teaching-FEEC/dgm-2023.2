import torch
from helper_functions import *
from torch.utils.data import Dataset
import numpy as np


class EEG(Dataset):

    def __init__(self, 
                 subject_id = 3, 
                 dataset_name="BNCI2014_001", 
                 channels = ['C3', 'Cz', 'C4'],
                 transform = None):
        
        self.raw_dataset     = MOABBDataset(dataset_name = dataset_name, subject_ids=[subject_id])
        self.prepro_dataset  = preprocessor(self.raw_dataset)
        self.windows_dataset = get_windows(self.prepro_dataset, picks = channels)
        self.data            = get_tensors_from_windows(self.windows_dataset)
        self.transform       = transform
        self.classes         = self.windows_dataset.datasets[0].windows.event_id
        
    def __len__(self):
        return self.data[0].shape[0]

    
    def __getitem__(self,idx):
        
        # sample = {'signal': torch.from_numpy(self.data[0])[idx], 'label': torch.from_numpy(self.data[1])[idx]}
        
        sample = (torch.from_numpy(np.expand_dims(self.data[0], axis = 1))[idx], torch.from_numpy(self.data[1])[idx])
        
        if self.transform:
            sample = self.transform(sample)
            
        return sample
