#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : AttendanceProject.py
import os

import cv2
import face_recognition


def getFaceEncode(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = None
    try:
        encode = face_recognition.face_encodings(img)[0]
    except IndexError as e:
        print(e)
    finally:
        return encode


def drawFace(img, name, distance):
    faceLoc = face_recognition.face_locations(img)[0]
    cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 255), 2)
    cv2.putText(img, f'{name} {round(distance, 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)


cap = cv2.VideoCapture(0)


def getList(staffdir):
    nameList = []
    nameEncodeList = []
    files = os.listdir(staffdir)
    for file in files:
        name = os.path.splitext(file)[0].upper()
        img = face_recognition.load_image_file(f'{staffdir}/{file}')
        encode = getFaceEncode(img)
        nameEncodeList.append(encode)
        nameList.append(name)
    return nameList, nameEncodeList


nameList, nameEncodeList = getList('staff')
while True:
    success, image = cap.read()
    encodeImage = getFaceEncode(image)
    if encodeImage is not None:
        results = face_recognition.compare_faces(nameEncodeList, encodeImage)
        faceDis = face_recognition.face_distance(nameEncodeList, encodeImage)
        if True in results:
            zipper = zip(results, faceDis, nameList)
            index = results.index(True)
            print(list(zipper)[index])
        else:
            cv2.putText(image, 'You are not identified', (100, 100), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (0, 0, 255), 2)
    else:
        print('No face found')
    cv2.imshow('webcam', image)
    cv2.waitKey(1)
