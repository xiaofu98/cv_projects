#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : authorization.py

import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('staffList.txt') as f:
    staffList = f.read().splitlines()

while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        if myData in staffList:
            print(myData)
            output = "authorized"
            myColor = (0,255,0)
        else:
            output = "Un-Authorized"
            myColor = (0, 0, 255)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 3)
        pts2 = barcode.rect
        cv2.putText(img,output,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.5,myColor,2)
    cv2.imshow('result', img)
    cv2.waitKey(1)
