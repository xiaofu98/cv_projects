#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : basic.py

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV默认使用BGR
print(pytesseract.image_to_string(img))
cv2.imshow("Result", img)
cv2.waitKey(0)