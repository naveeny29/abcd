from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from BillingUI import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exitB.clicked.connect(self.exit)
        self.ui.resetB.clicked.connect(self.reset)
        self.ui.billB.clicked.connect(self.billMethod)
    def reset(self):
        pass
    def billMethod(self):
        pp = int(self.ui.pani.text())*20
        mp = int(self.ui.masala.text())*25
        dp = int(self.ui.dahi.text())*30
        sp = int(self.ui.sweet.text())*30
        svp = int(self.ui.sev.text())*30
        pb = int(self.ui.pav.text())*40
        ct = int(self.ui.cutlet.text())*30
        kch = int(self.ui.kachori.text())*30
        sc = int(self.ui.samosa.text())*40
        gm = int(self.ui.gobi.text())*70
        nd = int(self.ui.noodles.text())*40
        cd = int(self.ui.cool.text())*20
        bill = pp+mp+dp+sp+svp+pb+ct+kch+sc+gm+nd+cd
        sgst = bill*0.05
        cgst = bill*0.05
        tot_bill = bill + sgst + cgst
        self.ui.label_16.setText("{:.2f}".format(bill))
        self.ui.label_17.setText("{:.2f}".format(sgst))
        self.ui.label_19.setText("{:.2f}".format(cgst))
        self.ui.label_21.setText("{:.2f}".format(tot_bill))
    def exit(self):
        sys.exit()



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

