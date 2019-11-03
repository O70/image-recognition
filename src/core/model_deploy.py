# -*- coding: utf-8 -*-
# @Time    : 10/31/19 10:38 AM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : model_deploy.py
# @Software: PyCharm
import os
from glob import glob
from heapq import nlargest

import cv2
from torch.utils.data import Dataset
import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.autograd import Variable
from torch.utils.data import DataLoader
from tqdm import tqdm
import albumentations as A
from core.model import get_net
from albumentations.pytorch import ToTensor
from albumentations.augmentations.transforms import CenterCrop
from itertools import chain
from collections import OrderedDict

dicts = {"W": 0, "P": 1, "Cg": 2,
         "S": 3, "H": 4, "rubbled": 5}
# dicts = {
#     'Cg/Cgm': 0,
#     'Cg/Cgc': 1,
#     'S/Sgx': 2,
#     'S/Spl': 3,
#     'S/Sm': 4,
#     'S/Smb': 5,
#     'S/Sx': 6,
#     'S/Sl': 7,
#     'S/Sr': 8,
#     'S/Sd': 9,
#     'S/Sdw': 10,
#     'S/Sds': 11,
#     'S/Sdi1(Sdi2)': 12,
#     'S/Si': 13,
#     'S/Sb': 14,
#     'SA/SAm(SAx)': 15,
#     'H/Hs': 16,
#     'H/Hm': 17,
#     'MS/Mm': 18,
#     'MS/Ml': 19,
#     'MS/Mb': 20,
#     'MS/Md': 21,
#     'MS/Mc': 22,
#     'C/C': 23,
#     'MT/M': 24,
#     'MR/MR': 25,
#     'W/W': 26,
#     'WP/WP': 27,
#     'P/P': 28,
#     'PG/PG': 29,
#     'G/G': 30,
#     'F/F': 31,
#     'R/R': 32,
#     'B/B': 33,
#     'Br/Br': 34,
#     'rubbled/rubbled': 35
# }
# W: 379
# P: 274
# PG: 95
# Cg: 495
# S: 679
# H: 133
# rubbled: 246
img_height = 384
img_width = 384
labels = []
predict = []


def get_keys(d, value):
    return [k for k, v in d.items() if v == value]


def get_test_transform(image_size):
    longest_size = max(image_size[0], image_size[1])
    return A.Compose([
        # Resize(int(config.img_height*00001.5),int(config.img_width*00001.5)),
        CenterCrop(img_height, img_width),
        A.LongestMaxSize(longest_size, interpolation=cv2.INTER_CUBIC),

        A.PadIfNeeded(image_size[0], image_size[1],
                      border_mode=cv2.BORDER_CONSTANT, value=0),

        A.Normalize(),
        ToTensor()
    ])


class LuoluDataset(Dataset):
    def __init__(self, label_list, train=True, test=False):
        self.test = test
        self.train = train
        imgs = []
        if self.test:
            for index, row in label_list.iterrows():
                imgs.append((row["filename"]))
            self.imgs = imgs
        else:
            for index, row in label_list.iterrows():
                imgs.append((row["filename"], row["label"]))
            self.imgs = imgs

    def __getitem__(self, index):
        if self.test:
            filename = self.imgs[index]
            img = cv2.imread(filename)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (int(img_height * 1.5), int(img_width * 1.5)))
            img = get_test_transform(img.shape)(image=img)["image"]
            return img, filename
        else:
            filename, label = self.imgs[index]
            img = cv2.imread(filename)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (int(img_height * 1.5), int(img_width * 1.5)))
            # img = get_train_transform(img.shape, augmentation=config.augmen_level)(image=img)["image"]
            return img, label

    def __len__(self):
        return len(self.imgs)


def get_files(root, mode):
    # for test
    if mode == "test":
        files = []
        for img in os.listdir(root):
            files.append(root + img)
        files = pd.DataFrame({"filename": files})
        return files
    elif mode != "test":
        # for train and val
        all_data_path, labels = [], []
        image_folders = list(map(lambda x: root + x, os.listdir(root)))
        all_images = list(chain.from_iterable(list(map(lambda x: glob(x + "/*"), image_folders))))
        print("loading train dataset")
        for file in tqdm(all_images):
            all_data_path.append(file)
            labels.append(int(file.split("/")[-2]))
        all_files = pd.DataFrame({"filename": all_data_path, "label": labels})
        return all_files
    else:
        print("check the mode please!")


def test(test_loader, model):
    # model.cuda()
    model.eval()
    tta = False
    global predict
    global labels
    results = []
    for i, (input, filepath) in enumerate(tqdm(test_loader)):
        filepath = [os.path.basename(x) for x in filepath]
        with torch.no_grad():
            image_var = Variable(input)
            # print('filepath: ', filepath)
            print(str(filepath).split('_'))
            class_label = str(filepath).split('_')[1]  # 提取类别信息
            print('True label: ', class_label.split("'")[-1])
            labels.append(dicts[class_label.split("'")[-1]])
            # print(input,input.shape)
            if tta == False:
                y_pred = model(image_var)
                smax = nn.Softmax(1)
                smax_out = smax(y_pred)

                size = 3
                max_index = list(map(list(smax_out[0]).index, nlargest(size, smax_out[0])))
                max_num = nlargest(size, smax_out[0].cpu().numpy())
                print("predict: ")
                #  class: get_keys(dicts, max_index[0])[0,1,2]
                #  degree of confidence: max_num[0,1,2]
                if len(get_keys(dicts, max_index[0])) != 0:
                    print("\t", get_keys(dicts, max_index[0])[0])
                print("\t", round(max_num[0], 6) * 100, "%")
                if len(get_keys(dicts, max_index[1])) != 0:
                    print("\t", get_keys(dicts, max_index[1])[0])
                print("\t", round(max_num[1], 6) * 100, "%")
                if len(get_keys(dicts, max_index[2])) != 0:
                    print("\t", get_keys(dicts, max_index[2])[0])
                print("\t", round(max_num[2], 6) * 100, "%")
                print("\n")

                print('******************')
                for ind in range(size):
                    # print(type(max_num[ind]), max_num[ind], type(max_num[ind].item()), max_num[ind].item(), round(max_num[ind].item(), 6), type(round(max_num[ind].item(), 6)))
                    results.append({ 'predict': round(max_num[ind].item(), 6), 'category': max_index[ind] })
                print(results)
                print('******************')
    return results

def recognition(imgpath):
    if not os.path.exists(imgpath):
        return []

    files = pd.DataFrame({ 'filename': [imgpath]})
    dataloader = DataLoader(LuoluDataset(files, test=True), batch_size=1, shuffle=False, pin_memory=False)

    model = get_net()
    pretrain = torch.load('./src/core/_checkpoint.pth.tar', map_location = 'cpu')
    model.load_state_dict(pretrain['state_dict'])

    return test(dataloader, model)

# if __name__ == "__main__":
#     model = get_net()
#     test_files = get_files("./test/", "test")

#     # load test set
#     test_dataloader = DataLoader(LuoluDataset(test_files, test=True), batch_size=1, shuffle=False, pin_memory=False)
#     # load trained model
#     # deploy cpu
#     pretrain = torch.load("./_checkpoint.pth.tar", map_location="cpu")
#     # model = nn.DataParallel(model)
#     model.load_state_dict(pretrain["state_dict"])
#     test(test_dataloader, model)
