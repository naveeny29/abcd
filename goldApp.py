from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from goldUI import *
from pandas import *
import matplotlib.pyplot as plt

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.display)
    def display(self):
        df = read_csv("D:\\Python\\PANDAS\\Gold Prices.csv")
        y = df['Year']
        x = df['Price']
        plt.plot(x, y, label='Gold Prices vs Year',color='#F986D9')
        plt.ylabel('Years')
        plt.xlabel('Price in Rs.')
        plt.legend()
        plt.show()
        



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

