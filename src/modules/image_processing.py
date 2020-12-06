# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:09:05 2020

@author: Yung
"""
import os
import torchvision as tv
import torchvision.transforms.functional as TF
from PIL import Image



def process_image(image_path: str, x_percent: float = 1.0, y_percent: float = 1.0):
    """
    
    Parameters
    ----------
    image_path : str
        Path of the image file in string
    x_percent : float
        cropping percentage of the image in width, between 0-1
    y_percent : float
        cropping percentage of the image in height, between 0-1

    Returns
    -------
    fully processed image in pytorch tensor

    """
    if x_percent >= 1 or y_percent >=1:
        return "Please redefine x_percent and/or y_percent as a float between 0-1"
    else:
        image = Image.open(image_path)
        
        # 1. get image as PIL file
        #   1A reduce it to greyscale
        # 2. get the image size as the pytorch tensor
        #   2A. tensor shape is (Channel, width, height)
        # 3. use centercrop at defined percantage * widtth or height
        # 4. push the cropped to torchvision resize to the size deisred
        # 5. return cropped and resized image tensor