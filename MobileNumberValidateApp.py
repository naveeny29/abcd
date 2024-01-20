from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from MobileNumberValidateUI import *
from re import *
class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.validate)
    def validate(self):
        num = self.ui.lineEdit.text()
        m = fullmatch('[6-9][0-9]{9}',num)
        
        if m!=None:
            self.ui.label_2.setText("Valid Mobile Number")
        else:
            self.ui.label_2.setText("Invalid Mobile Number")
        



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

