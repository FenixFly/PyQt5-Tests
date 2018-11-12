# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QLabel)
from PyQt5.QtGui import QFont  
from PyQt5.QtCore import QCoreApplication
  
class Test(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))  
        
        self.text = QLabel("It's an old label!", self)
        self.text.move(100,10)
           
        changeBtn = QPushButton('Change Label', self)
        changeBtn.clicked.connect(self.changeLabel)
        changeBtn.resize(100, 30)
        changeBtn.move(100, 50) 
        
        exitBtn = QPushButton('Exit Button', self)
        exitBtn.clicked.connect(self.close)
        exitBtn.setToolTip('This is a <b>Button</b> widget')
        exitBtn.resize(100, 30)
        exitBtn.move(100, 100)       
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('ButtonWindow')    
        self.show()
        
    def changeLabel(self):
        self.text.setText('Its a new label now!')
        self.text.adjustSize()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Test()
    sys.exit(app.exec_())