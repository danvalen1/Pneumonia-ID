# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:09:05 2020

@author: Yung
"""
import os
import torch
import torch.nn as nn #neural network
import torchvision as tv
import torchvision.transforms as TF



## update this to sequential?
def preprocess_image_flat(path_list, img_h=120, img_w=120):
    outlist = [] #intialize blank list
    for path in path_list: #for all file path
        resizer = TF.Resize((img_h, img_w)) #define resizer per new_h and new_w
        im = tv.io.read_image(path).type(torch.float) #read image as pytorch float tensor
        im = resizer(im) #resize image
        if im.shape[0] != 1:
            im = TF.functional.rgb_to_grayscale(im)
        normalizer = TF.Normalize(im.mean(), im.std()) #initialize normalizer
        im = normalizer(im) # return normalized pytorch float tensor
        im = torch.flatten(im)
        outlist.append(im)
    return torch.stack(outlist) # return all tensors in a stacked tensor


class linear_prototype(nn.Module):
    def __init__(self, img_h, img_w):
        super().__init__()
        #define sizes here
        self.h = img_h
        self.w = img_w
        self.longshape = img_h*img_w
        self.linear1 = nn.Linear(self.longshape, 320)
        self.relu1 = nn.ReLU()
        self.linear2 = nn.Linear(320, 1)
        self.term_act = nn.Sigmoid()
        self.relu2 = nn.ReLU()
    
    def forward(self, x):
        # preprocess the input image
        #============ Layer1==============#
        x = self.linear1(x)
        x = self.relu1(x)
        #============Layer2==============#
        x = self.linear2(x)
        #x = self.softmax(x)
        x = self.term_act(x)
        return self.relu2(x)