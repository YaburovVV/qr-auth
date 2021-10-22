#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import qrcode
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QLabel)
from PyQt5.QtGui import QPixmap


class QRExperiment(QWidget):

    imgFile = 'hello.png'

    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.generateQRCode("hello world")
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        sld.valueChanged.connect(self.generateQRCode)

        self.setGeometry(300, 300, 250, 500)
        self.setWindowTitle('Signal & slot')
        self.show()

    # Generate QR Code
    def generateQRCode(self, qrText):
        img = qrcode.make(qrText)
        img.save(QRExperiment.imgFile)
        pixmap = QPixmap(QRExperiment.imgFile)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QRExperiment()
    sys.exit(app.exec_())
