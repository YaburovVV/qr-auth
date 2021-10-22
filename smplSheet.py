#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QPushButton
app = QApplication([])
app.setStyleSheet("QPushButton { margin: 20ex; }")
button = QPushButton('Hello World')
button.show()
app.exec()