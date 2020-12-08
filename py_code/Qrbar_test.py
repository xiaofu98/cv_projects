#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : Qrbar_test.py

import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('qrcode.png')
for barcode in decode(img):
    print(barcode.data.decode('utf-8'))
    print(barcode.data)
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    print(pts)
    print(barcode.rect)
