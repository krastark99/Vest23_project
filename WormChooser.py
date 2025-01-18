from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor
from PyQt5 import QtGui
import Image
import numpy as np
import os
import sys


app = QApplication([])


winres = QWidget()
winres.resize(600,550)
winres.setWindowTitle("Результат")
winres.hide()




background = QLabel(winres)
colorofworm = QLabel(winres)
conturofworm = QLabel(winres)
clothes = QLabel(winres)




file = sys.argv[0]
dirname = os.path.dirname(file)






win = QWidget()
win.resize(500, 500)
win.setWindowTitle("Тест")
win.show()

row = QVBoxLayout()
col1 = QHBoxLayout()
col2 = QHBoxLayout()
col3 = QHBoxLayout()
col4 = QHBoxLayout()
col5 = QHBoxLayout()
col6 = QHBoxLayout()
col7 = QHBoxLayout()
col8 = QHBoxLayout()
col9 = QHBoxLayout()
col10 = QHBoxLayout()
col11 = QHBoxLayout()
col12 = QHBoxLayout()

NameOfTest = QLabel("Тест: Який ви хробачок?")
NameOfTest.setAlignment(Qt.AlignCenter)

btn_create = QPushButton("Створити")
#WhatName = QLabel("Введіть ваше ім'я:")
#AddName = QLineEdit("")
#AddName.setPlaceholderText("Введіть ім'я")



WhatColor = QLabel("Оберіть фрукт, який би ви з'їли:")
WhatDrink = QLabel("Оберіть напій, який вам більше до вподоби:")
WhatWrite = QLabel("Оберіть чим би написали своє ім'я")

AddDrink1 = QRadioButton("Коктейль")
AddDrink2 = QRadioButton("Чай")
AddDrink3 = QRadioButton("Вода")
AddDrink4 = QRadioButton("Сік")
AddDrink5 = QRadioButton("Молоко")

AddColor = QComboBox()



AddWrite1 = QCheckBox("Ручка")
AddWrite2 = QCheckBox("Олівець")
AddWrite3 = QCheckBox("Перо")
AddWrite4 = QCheckBox("Морквина")

AddWritings = QButtonGroup()
AddWritings.addButton(AddWrite1)
AddWritings.addButton(AddWrite2)
AddWritings.addButton(AddWrite3)
AddWritings.addButton(AddWrite4)

#qlabels

KavaAdd = QLabel(win)
CocktailAdd = QLabel(win)
JuiceAdd = QLabel(win)
WaterAdd = QLabel(win)
MilkAdd = QLabel(win)

PenAdd = QLabel(win)
PencilAdd = QLabel(win)
FeatherAdd = QLabel(win)
CarrotAdd = QLabel(win)


Lilworm1 = QLabel(win)
Lilworm2 = QLabel(win)

Lilworm1.setAlignment(Qt.AlignLeft)
Lilworm2.setAlignment(Qt.AlignRight)



pixmap = QtGui.QPixmap(os.path.join(dirname,"kava.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
KavaAdd.setPixmap(pixmap)



pixmap = QtGui.QPixmap(os.path.join(dirname,"cocktail.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
CocktailAdd.setPixmap(pixmap)


pixmap = QtGui.QPixmap(os.path.join(dirname,"water.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
WaterAdd.setPixmap(pixmap)

pixmap = QtGui.QPixmap(os.path.join(dirname,"juice.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
JuiceAdd.setPixmap(pixmap)

pixmap = QtGui.QPixmap(os.path.join(dirname,"milk.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
MilkAdd.setPixmap(pixmap)

pixmap = QtGui.QPixmap(os.path.join(dirname,"lilworm1.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
Lilworm1.setPixmap(pixmap)

pixmap = QtGui.QPixmap(os.path.join(dirname,"lilworm2.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
Lilworm2.setPixmap(pixmap)


pixmap = QtGui.QPixmap(os.path.join(dirname,"pen.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
PenAdd.setPixmap(pixmap)



pixmap = QtGui.QPixmap(os.path.join(dirname,"pencil.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
PencilAdd.setPixmap(pixmap)


pixmap = QtGui.QPixmap(os.path.join(dirname,"feather.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
FeatherAdd.setPixmap(pixmap)

pixmap = QtGui.QPixmap(os.path.join(dirname,"carrot.png"))
pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)
CarrotAdd.setPixmap(pixmap)



#end of qlabels



#додати зв'язок з результатом
col1.addWidget(Lilworm1)
col1.addWidget(NameOfTest)
col1.addWidget(Lilworm2)
col12.addWidget(btn_create)
#col2.addWidget(WhatName)
#col3.addWidget(AddName)
#col3.addWidget()


col8.addWidget(WhatColor)
col8.addWidget(AddColor)


col4.addWidget(WhatDrink)

col5.addWidget(AddDrink1)
col5.addWidget(CocktailAdd)
col5.addWidget(AddDrink2)
col5.addWidget(KavaAdd)
col6.addWidget(AddDrink3)
col6.addWidget(WaterAdd)
col6.addWidget(AddDrink4)
col6.addWidget(JuiceAdd)
col7.addWidget(AddDrink5)
col7.addWidget(MilkAdd)
#col7.addWidget()
#col7.addWidget()
col9.addWidget(WhatWrite)
col10.addWidget(AddWrite1)
col10.addWidget(PenAdd)
col10.addWidget(AddWrite2)
col10.addWidget(PencilAdd)
col11.addWidget(AddWrite3)
col11.addWidget(FeatherAdd)
col11.addWidget(AddWrite4)
col11.addWidget(CarrotAdd)

color_list = ["Полуниця", "Мандарин", "Лимон", "Лайм", "Інжир", "Лохина" ,"Малина", "Виноград"]
AddColor.addItems(color_list)





def create_winres():
    winres.hide()     
    if AddDrink3.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname, "athome1.png"))
    if AddDrink4.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname, "garden.png"))
    if AddDrink1.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname, "restaraunt2.png"))
    if AddDrink2.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname, "beach.png"))
    if AddDrink5.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname, "snowy.png"))
    
    pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
    background.setPixmap(pixmap)
    background.show()
    background.move(50,0)


    index = AddColor.currentIndex()
    if index == 0:
        pixmap = QtGui.QPixmap(os.path.join(dirname,"colorworm1.png"))
    if index == 1:
        pixmap = QtGui.QPixmap(os.path.join(dirname,"orangecol.png"))
    if index == 2:
        pixmap = QtGui.QPixmap(os.path.join(dirname,"yellowcol.png"))
    if index == 3:
        pixmap = QtGui.QPixmap(os.path.join(dirname,"greencol.png"))
    if index == 4:
        pixmap = QtGui.QPixmap(os.path.join(dirname,"cyancol.png"))
    if index == 5:
        pixmap = QtGui.QPixmap(os.path.join(dirname,"bluecol.png"))
    if index == 6:
        pixmap = QtGui.QPixmap(os.path.join(dirname,"pinkcol.png"))
    if index == 7:
        pixmap = QtGui.QPixmap(os.path.join(dirname,"purplecol.png"))


    pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
    colorofworm.setPixmap(pixmap)
    colorofworm.show()
    colorofworm.move(60,0)

    pixmap = QtGui.QPixmap(os.path.join(dirname,"wormcontur.png"))
    pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
    conturofworm.setPixmap(pixmap)
    conturofworm.show()
    conturofworm.move(60,0)
    
    if AddWrite1.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname,"official.png"))
    if AddWrite2.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname,"packet.png"))
    if AddWrite3.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname,"crown.png"))
    if AddWrite4.isChecked():
        pixmap = QtGui.QPixmap(os.path.join(dirname,"icecream.png"))
    
    pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
    clothes.setPixmap(pixmap)
    clothes.show()
    clothes.move(60,0)

    winres.show()

    

row.addLayout(col1)
row.addLayout(col2)
row.addLayout(col3)
row.addLayout(col4)
row.addLayout(col5)
row.addLayout(col6)
row.addLayout(col7)
row.addLayout(col8)
row.addLayout(col9)
row.addLayout(col10)
row.addLayout(col11)
row.addLayout(col12)


btn_create.clicked.connect(create_winres)

win.setWindowIcon(QtGui.QIcon(os.path.join(dirname, "lilworm1.png")))
                  
winres.setWindowIcon(QtGui.QIcon(os.path.join(dirname,"lilworm2.png")))

win.setLayout(row)
app.exec()
