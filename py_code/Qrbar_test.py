#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : Qrbar_test.py

import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('qrcode_rotated.png')
for barcode in decode(img):
    print(barcode.data.decode('utf-8'))
    print(barcode.data)
    print(barcode.rect)
