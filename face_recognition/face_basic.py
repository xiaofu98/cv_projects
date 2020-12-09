#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : face_basic.py
import os

import cv2
import face_recognition

os.makedirs('faces', exist_ok=True)


def convertImg(path):
    img = face_recognition.load_image_file(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def getFace(img):
    faceLoc = face_recognition.face_locations(img)[0]
    encode = face_recognition.face_encodings(img)[0]
    cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 255), 2)
    return encode


imgElon = convertImg('faces/Elon-Musk.jpg')
imgTest = convertImg('faces/Elon-Test.jpg')
imgGates = convertImg('faces/gates.jpg')

encodeElon = getFace(imgElon)
encodeElonTest = getFace(imgTest)
encodeGates = getFace(imgGates)

results = face_recognition.compare_faces([encodeElon, encodeGates], encodeElonTest)
faceDis = face_recognition.face_distance([encodeElon, encodeGates], encodeElonTest)
print(results, faceDis)

cv2.putText(imgTest, f'{results[0]} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
cv2.putText(imgGates, f'{results[1]} {round(faceDis[1], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.imshow('Bill Gates', imgGates)
cv2.waitKey(0)
