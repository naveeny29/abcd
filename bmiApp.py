from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from bmiUI import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculateB.clicked.connect(self.bmi)
        self.ui.resetB.clicked.connect(self.reset)
        self.ui.exitB.clicked.connect(self.exit)
    def reset(self):
        self.ui.height.clear()
        self.ui.weight.clear()
    def exit(self):
        sys.exit()
    def bmi(self):
        w = float(self.ui.weight.text())
        height = float(self.ui.height.text())
        h = height*0.3048
        bmi = w/(h**2)
        if 0<=bmi<18.5:
            QtWidgets.QMessageBox.about(self,"Status","Under Weight")
        elif 18.5<=bmi<=24.9:
            QtWidgets.QMessageBox.about(self,"Status","Normal Weight")
        elif 24.9<bmi<=29.9:
            QtWidgets.QMessageBox.about(self,"Status","Pre Obesity")
        elif 29.9<bmi<=34.9:
            QtWidgets.QMessageBox.about(self,"Status","Pre Obesity - 1")
        elif 34.9<bmi<=39.9:
            QtWidgets.QMessageBox.about(self,"Status","Pre Obesity - 2")
        elif bmi>39.9:
            QtWidgets.QMessageBox.about(self,"Status","Pre Obesity - 3")
        
    



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

