#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : face_basic.py
import cv2
import numpy as np
import os
import face_recognition

os.makedirs('faces', exist_ok=True)

imgElon = face_recognition.load_image_file('faces/Elon-Musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('faces/Elon-Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

imgGates = face_recognition.load_image_file('faces/gates.jpg')
imgGates = cv2.cvtColor(imgGates, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeElonTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 0, 255), 2)

faceLocGates = face_recognition.face_locations(imgGates)[0]
encodeGates = face_recognition.face_encodings(imgGates)[0]
cv2.rectangle(imgGates, (faceLocGates[3], faceLocGates[0]), (faceLocGates[1], faceLocGates[2]), (0, 0, 255), 2)

results = face_recognition.compare_faces([encodeElon, encodeGates], encodeElonTest)
print(results)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.imshow('Bill Gates', imgGates)
cv2.waitKey(0)
