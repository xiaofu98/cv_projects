#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : main.py
import cv2
import os

imgPath = 'images'
os.makedirs('images', exist_ok=True)
myFolders = os.listdir(imgPath)

for folder in myFolders:
    path = imgPath + '/' + folder
    images = []
    myList = os.listdir(path)
    print(f'Total no of images detected {len(myList)}')
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        curImg = cv2.resize(curImg, (0, 0), None, 0.2, 0.2)
        images.append(curImg)
        cv2.waitKey(1)
    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if status == cv2.STITCHER_OK:
        print('Panorame Generated')
        cv2.imshow(folder, result)
    else:
        print('Panorma Generation Unsuccessful!')
cv2.waitKey(0)
