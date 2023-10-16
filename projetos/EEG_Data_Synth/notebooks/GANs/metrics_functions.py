from gan_input_functions import *
from helper_functions import *


import torch
from torch import nn
import torch.nn.functional as F

import numpy as np


def generate_samples_with_labels(label, n_samples, generator, channel = None, extra_dim = True):
    '''
    Function for generating samples, once the generator has been trained
        label: label of the movement to be sampled. See dictionary below
        {'feet': 0, 'left_hand': 1, 'right_hand': 2, 'tongue': 3}
        n_samples: number of samples to be generated
        channel: electrode {'C3': 0, 'Cz': 1, 'C4': 2} -> Default: All channels
        generator: the trained generator
    '''

    if channel == None:
        noise_4_gen = get_noise(n_samples, z_dim)
        label = get_one_hot_labels(torch.Tensor([label]).long(), n_classes).repeat(n_samples,1)
        
        noise_and_labels = combine_vectors(noise_4_gen, label)
        fake = gen(noise_and_labels)

        if extra_dim == False:
            fake = fake.reshape((fake.shape[0], fake.shape[2], fake.shape[3]))
        return fake
    else:
        noise_4_gen = get_noise(n_samples, z_dim)
        label = get_one_hot_labels(torch.Tensor([label]).long(), n_classes).repeat(n_samples,1)
        
        noise_and_labels = combine_vectors(noise_4_gen, label)
        fake = gen(noise_and_labels)
        filtered_channel_fake = torch.select(fake, dim = 2, index = channel)
        
        if extra_dim == False:
            filtered_channel_fake = filtered_channel_fake.reshape((filtered_channel_fake.shape[0], filtered_channel_fake.shape[2]))

        return filtered_channel_fake


def generate_samples_for_classification(n_samples, generator):
    '''
    Function for generating equal label samples for the classifier. 
        n_samples: number of samples to be generated
        generator: the trained generator
    '''
    n_samples = n_samples
    n_samples_partial = int(n_samples/n_classes)
    noise_4_gen = get_noise(n_samples, z_dim)
    
    label = [0,1,2,3]
    
    label = [get_one_hot_labels(torch.Tensor([i]).long(), n_classes).repeat(n_samples_partial,1) for i in label]
    
    label_concat = torch.zeros_like(torch.Tensor(0,4))
    for i in range(len(label)):
        label_concat = torch.cat((label_concat,label[i]), 0)
    
    noise_and_labels = combine_vectors(noise_4_gen, label_concat)
    
    fake = generator(noise_and_labels)

    return fake


def filter_label_and_channel(eeg_data, classe, canal):
    '''
    Function to filter label and channel of original eeg data. 
        eeg_data: raw eeg data
        classe: class of movement
        canal: electrode --   {'C3': 0, 'Cz': 1, 'C4': 2}
    '''

    
    mask = torch.where(eeg_data[:][1] == classe, 1, 0)
    filtered_eeg = eeg_data[:][0][torch.nonzero(mask).flatten()]
    filtered_eeg = filtered_eeg.reshape((filtered_eeg.shape[0], filtered_eeg.shape[2], filtered_eeg.shape[3] ))
    filtered_channel_eeg = torch.select(filtered_eeg, dim = 1, index = canal)

    return filtered_channel_eeg
