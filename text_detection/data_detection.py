#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : data_detection.py

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV默认使用BGR

boxes = pytesseract.image_to_data(img)
hImg, wImg, _ = img.shape
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b,len(b))
        if len(b) == 12:
            x, y, x1, y1 = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (x+x1, y+y1), (0, 0, 255), 3)
            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
