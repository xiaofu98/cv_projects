#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : chinese_detection.py

import pytesseract
import cv2

path = 'test.png'
img = cv2.imread(path, 0)


# 需要中文包，并配置环境变量
def img_recognition(image, lang='chi_sim'):
    code = pytesseract.image_to_string(image, lang)
    print(code)


if __name__ == '__main__':
    img_recognition(img)