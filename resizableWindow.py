# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QApplication
    

app = QApplication(sys.argv)    #создание объекта приложения
w = QWidget()                   #виджет без родителя - окно
w.resize(500,500)               #размер окна
w.move(300,300)                 #положение окна
w.setWindowTitle("Hello world") #имя окна
w.show()                        #отображение окна
sys.exit(app.exec_())