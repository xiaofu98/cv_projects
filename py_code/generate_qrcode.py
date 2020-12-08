#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @File    : generate_qrcode.py

from qrcode.main import QRCode
import os

os.makedirs('qrcode', exist_ok=True)
path = 'staffList.txt'
qr = QRCode()


def QrCodeBatch(pathfile):
    with open(pathfile) as f:
        staffList = f.read().splitlines()
    i = 0
    for name in staffList:
        qr.add_data(name)
        qr.make(fit=True)
        img = qr.make_image()
        filename = name + '.png'
        img.save(os.path.join('qrcode', filename))
        qr.clear()
        i = i + 1
        print('done No. ' + str(i))
    print('finished' + str(i))


if __name__ == '__main__':
    QrCodeBatch(path)
