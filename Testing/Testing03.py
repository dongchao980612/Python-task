
# -*- coding: utf-8 -*-
# Time    : 2025/8/25 10:14
# File    : Testing03.py
# Software: PyCharm

import torch
from torchvision.io import read_image

if __name__ == '__main__':
    img = read_image('example-image.png')
    print('Image shape:', img.shape)
    # Image shape: torch.Size([3, 252, 221])
    print('Number of channels:', img.shape[0])
    #Number of channels: 3
    print('Image data type:', img.dtype)
    # Image data type: torch.uint8
    print(img[:, 100:102, 100:102])