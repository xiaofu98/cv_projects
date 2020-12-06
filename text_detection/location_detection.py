#!/usr/bin/pyty1on3
# -*- coding: utf-8 -*-
# @File    : location_detection.py

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV默认使用BGR

boxes = pytesseract.image_to_boxes(img)
wImg, hImg, _ = img.shape
print(wImg,hImg)
for b in boxes.splitlines():
    b = b.split(' ')
    x, y, x1, y1 = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    print(x, y, x1, y1)
    cv2.rectangle(img, (x,  y), (x1,  y1), (0, 255, 0), 3)
    # cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
