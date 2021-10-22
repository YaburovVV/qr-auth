#!/usr/bin/env python

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
button = QPushButton('Hello World')
button2 = QPushButton('Hello 2')
button3 = QPushButton('Hello 3')
layout.addWidget(button)
layout.addWidget(button2)
layout.addWidget(button3)
window.setLayout(layout)
window.show()
app.exec()