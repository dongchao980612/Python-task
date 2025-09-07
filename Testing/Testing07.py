
# -*- coding: utf-8 -*-
# Time    : 2025/8/25 11:24
# File    : Testing07.py
# Software: PyCharm

import torchvision
from torchvision import transforms
from torch.utils.data import Subset
from torch.utils.data import DataLoader
import  torch
import  torch.nn  as  nn
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import torchvision
from torchvision import transforms
from torch.utils.data import Subset
from torch.utils.data import DataLoader
import  torch
import  torch.nn  as  nn
def train(model, num_epochs, train_dl, valid_dl):
    loss_hist_train = [0] * num_epochs
    accuracy_hist_train = [0] * num_epochs
    loss_hist_valid = [0] * num_epochs
    accuracy_hist_valid = [0] * num_epochs
    for epoch in range(num_epochs):
        model.train()
        for x_batch, y_batch in train_dl:
            pred = model(x_batch)[:, 0]
            loss = loss_fn(pred, y_batch.float())
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            loss_hist_train[epoch] += loss.item()*y_batch.size(0)
            is_correct = ((pred>=0.5).float() == y_batch).float()
            accuracy_hist_train[epoch] += is_correct.sum()
        loss_hist_train[epoch] /= len(train_dl.dataset)
        accuracy_hist_train[epoch] /= len(train_dl.dataset)

    model.eval()
    with torch.no_grad():
        for x_batch, y_batch in valid_dl:
            pred = model(x_batch)[:, 0]
            loss = loss_fn(pred, y_batch.float())
            loss_hist_valid[epoch] += \
            loss.item() * y_batch.size(0)
            is_correct = \
            ((pred>=0.5).float() == y_batch).float()
            accuracy_hist_valid[epoch] += is_correct.sum()
    loss_hist_valid[epoch] /= len(valid_dl.dataset)
    accuracy_hist_valid[epoch] /= len(valid_dl.dataset)

    print(f'Epoch {epoch+1} accuracy: {accuracy_hist_train[epoch]:.4f} val_accuracy: {accuracy_hist_valid[epoch]:.4f}')

    return loss_hist_train, loss_hist_valid, accuracy_hist_train, accuracy_hist_valid

if __name__ == '__main__':
    image_path = './'
    transform = transforms.Compose([
        transforms.ToTensor()]
    )


    celeba_train_dataset = torchvision.datasets.CelebA(image_path, split='train',target_type='attr', download=True)
    celeba_valid_dataset = torchvision.datasets.CelebA(image_path, split='valid',target_type='attr', download=True)
    celeba_test_dataset = torchvision.datasets.CelebA(image_path, split='test',target_type='attr', download=True)

    print('Train set:', len(celeba_train_dataset))
    print('Validation set:', len(celeba_valid_dataset))
    print('Test set:', len(celeba_test_dataset))

    fig = plt.figure(figsize=(16, 8.5))
    ## Column 1: cropping to a bounding-box
    ax = fig.add_subplot(2, 5, 1)
    img, attr = celeba_train_dataset[0]
    ax.set_title('Crop to a \nbounding-box', size=15)
    ax.imshow(img)
    ax = fig.add_subplot(2, 5, 6)
    img_cropped = transforms.functional.crop(img, 50, 20, 128, 128)
    ax.imshow(img_cropped)

    ## Column 2: flipping (horizontally)
    ax = fig.add_subplot(2, 5, 2)
    ax = fig.add_subplot(2, 5, 2)
    img, attr = celeba_train_dataset[1]
    ax.set_title('Flip (horizontal)', size=15)
    ax.imshow(img)
    ax = fig.add_subplot(2, 5, 7)
    img_flipped = transforms.functional.hflip(img)
    ax.imshow(img_flipped)

    ## Column 3: adjust contrast
    ax = fig.add_subplot(2, 5, 3)
    img, attr = celeba_train_dataset[2]
    ax.set_title('Adjust constrast', size=15)
    ax.imshow(img)
    ax = fig.add_subplot(2, 5, 8)
    img_adj_contrast = transforms.functional.adjust_contrast(img, contrast_factor = 2)
    ax.imshow(img_adj_contrast)

    ## Column 4: adjust brightness
    ax = fig.add_subplot(2, 5, 4)
    img, attr = celeba_train_dataset[3]
    ax.set_title('Adjust brightness', size=15)
    ax.imshow(img)
    ax = fig.add_subplot(2, 5, 9)
    img_adj_brightness = transforms.functional.adjust_brightness(img, brightness_factor = 1.3)
    ax.imshow(img_adj_brightness)

    ## Column 5: cropping from image center
    ax = fig.add_subplot(2, 5, 5)
    img, attr = celeba_train_dataset[4]
    ax.set_title('Center crop\nand resize', size=15)
    ax.imshow(img)
    ax = fig.add_subplot(2, 5, 10)

    img_center_crop = transforms.functional.center_crop(img, [0.7 * 218, 0.7 * 178])
    img_resized = transforms.functional.resize(img_center_crop, size = (218, 178))
    ax.imshow(img_resized)
    plt.show()

    get_smile = lambda attr: attr[18]

    transform_train = transforms.Compose([
        transforms.RandomCrop([178, 178]),
        transforms.RandomHorizontalFlip(),
        transforms.Resize([64, 64]),
        transforms.ToTensor(),])

    from torch.utils.data import DataLoader
    celeba_train_dataset = torchvision.datasets.CelebA(image_path, split = 'train',target_type = 'attr', download = False,
    transform = transform_train, target_transform = get_smile)

    torch.manual_seed(1)
    data_loader = DataLoader(celeba_train_dataset, batch_size=2)
    fig = plt.figure(figsize=(15, 6))
    num_epochs = 5

    # for j in range(num_epochs):
    #     img_batch, label_batch = next(iter(data_loader))
    #     img = img_batch[0]
    #     ax = fig.add_subplot(2, 5, j + 1)
    #     ax.set_xticks([])
    #     ax.set_yticks([])
    #     ax.set_title(f'Epoch {j}:', size=15)
    #     ax.imshow(img.permute(1, 2, 0))
    #     img = img_batch[1]
    #     ax = fig.add_subplot(2, 5, j + 6)
    #     ax.set_xticks([])
    #     ax.set_yticks([])
    #     ax.imshow(img.permute(1, 2, 0))
    # plt.show()

    celeba_valid_dataset = torchvision.datasets.CelebA(image_path, split = 'valid',target_type = 'attr', download = False,transform = transform, target_transform = get_smile)

    celeba_test_dataset = torchvision.datasets.CelebA(image_path, split = 'test',target_type = 'attr', download = False,transform = transform, target_transform = get_smile)

    from torch.utils.data import Subset
    celeba_train_dataset = Subset(celeba_train_dataset,torch.arange(16000))
    celeba_valid_dataset = Subset(celeba_valid_dataset,torch.arange(1000))
    print('Train set:', len(celeba_train_dataset))
    print('Validation set:', len(celeba_valid_dataset))

    batch_size = 32
    torch.manual_seed(1)
    train_dl = DataLoader(celeba_train_dataset,batch_size, shuffle = True)
    valid_dl = DataLoader(celeba_valid_dataset,batch_size, shuffle = False)
    test_dl = DataLoader(celeba_test_dataset,batch_size, shuffle = False)


    model = nn.Sequential()
    model.add_module('conv1',nn.Conv2d(in_channels = 3, out_channels = 32,kernel_size = 3, padding = 1))

    model.add_module('relu1', nn.ReLU())
    model.add_module('pool1', nn.MaxPool2d(kernel_size=2))
    model.add_module('dropout1', nn.Dropout(p=0.5))

    model.add_module('conv2',nn.Conv2d(in_channels = 32, out_channels = 64,kernel_size = 3, padding = 1))
    model.add_module('relu2', nn.ReLU())
    model.add_module('pool2', nn.MaxPool2d(kernel_size=2))
    model.add_module('dropout2', nn.Dropout(p=0.5))

    model.add_module('conv3',nn.Conv2d(in_channels = 64, out_channels = 128,kernel_size = 3, padding = 1))
    model.add_module('relu3', nn.ReLU())
    model.add_module('pool3', nn.MaxPool2d(kernel_size=2))

    model.add_module('conv4',nn.Conv2d(in_channels = 128, out_channels = 256,kernel_size = 3, padding = 1))
    model.add_module('relu4', nn.ReLU())

    x = torch.ones((4, 3, 64, 64))
    print(model(x).shape)

    model.add_module('pool4', nn.AvgPool2d(kernel_size=8))
    model.add_module('flatten', nn.Flatten())
    x = torch.ones((4, 3, 64, 64))
    print(model(x).shape)

    model.add_module('fc', nn.Linear(256, 1))
    model.add_module('sigmoid', nn.Sigmoid())
    x = torch.ones((4, 3, 64, 64))
    print(model(x).shape)

    loss_fn = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    torch.manual_seed(1)
    num_epochs = 30
    hist = train(model, num_epochs, train_dl, valid_dl)

    x_arr = np.arange(len(hist[0])) + 1
    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(x_arr, hist[0], '-o', label='Train loss')
    ax.plot(x_arr, hist[1], '--<', label='Validation loss')
    ax.legend(fontsize=15)
    ax = fig.add_subplot(1, 2, 2)
    ax.plot(x_arr, hist[2], '-o', label='Train acc.')
    ax.plot(x_arr, hist[3], '--<',label = 'Validation acc.')
    ax.legend(fontsize=15)
    ax.set_xlabel('Epoch', size=15)
    ax.set_ylabel('Accuracy', size=15)
    plt.show()

    accuracy_test = 0
    model.eval()
    with torch.no_grad():
        for x_batch, y_batch in test_dl:
            pred = model(x_batch)[:, 0]
            is_correct = ((pred >= 0.5).float() == y_batch).float()

    accuracy_test += is_correct.sum()
    accuracy_test /= len(test_dl.dataset)
    print(f'Test accuracy: {accuracy_test:.4f}')

    pred = model(x_batch)[:, 0] * 100
    fig = plt.figure(figsize=(15, 7))
    for j in range(10, 20):
        ax = fig.add_subplot(2, 5, j - 10 + 1)
        ax.set_xticks([]);ax.set_yticks([])

        ax.imshow(x_batch[j].permute(1, 2, 0))

        if y_batch[j] == 1:
            label = 'Smile'
        else:
            label = 'Not Smile'

        ax.text(0.5, -0.15,f'GT: {label:s}\nPr(Smile)={pred[j]:.0f}%',size = 16,horizontalalignment = 'center',verticalalignment = 'center',transform = ax.transAxes)
    plt.show()