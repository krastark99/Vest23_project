from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

app = QApplication([])

win = QWidget()
win.resize(1000, 1000)
win.setWindowTitle("TestProgram")
win.show()

p = QLabel("")
w = QVBoxLayout()


p.hide()
piximg = QPixmap('Pic1.jpg')
wi = p.width()
h = p.height()
piximg = piximg.scaled(800, 800, Qt.KeepAspectRatio)
p.setPixmap(piximg)
p.show()


w.addWidget(p)
win.setLayout(w)



app.exec()