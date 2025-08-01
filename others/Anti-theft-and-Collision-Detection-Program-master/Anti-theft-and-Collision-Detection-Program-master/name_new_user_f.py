from PyQt5 import QtWidgets
from name_new_user import Ui_name_new_user
#from PyQt5.QtWidgets import QApplication
#import sys

class name_new_userwindow(QtWidgets.QMainWindow,Ui_name_new_user):
    def comparecode(self):
        pass

    def backspacecode(self):
        self.lineEdit.backspace()

    def appendcode(self,n):
        if self.cap:
            self.lineEdit.insert(str(n).upper())
        else:
            self.lineEdit.insert(str(n))


    def cap_switch(self):
        if self.cap:
            self.bcap.setStyleSheet("color: white; border: 3px solid yellow;")
            self.cap=0
            self.bq.setText("q")
            self.bw.setText("w")
            self.be.setText("e")
            self.br.setText("r")
            self.bt.setText("t")
            self.by.setText("y")
            self.bu.setText("u")
            self.bi.setText("i")
            self.bo.setText("o")
            self.bp.setText("p")
            self.ba.setText("a")
            self.bs.setText("s")
            self.bd.setText("d")
            self.bf.setText("f")
            self.bg.setText("g")
            self.bh.setText("h")
            self.bj.setText("j")
            self.bk.setText("k")
            self.bl.setText("l")
            self.bz.setText("z")
            self.bx.setText("x")
            self.bc.setText("c")
            self.bv.setText("v")
            self.bb.setText("b")
            self.bn.setText("n")
            self.bm.setText("m")

        else:
            self.cap=1
            self.bcap.setStyleSheet("color: white; border: 3px solid blue;")
            self.bq.setText("Q")
            self.bw.setText("W")
            self.be.setText("E")
            self.br.setText("R")
            self.bt.setText("T")
            self.by.setText("Y")
            self.bu.setText("U")
            self.bi.setText("I")
            self.bo.setText("O")
            self.bp.setText("P")
            self.ba.setText("A")
            self.bs.setText("S")
            self.bd.setText("D")
            self.bf.setText("F")
            self.bg.setText("G")
            self.bh.setText("H")
            self.bj.setText("J")
            self.bk.setText("K")
            self.bl.setText("L")
            self.bz.setText("Z")
            self.bx.setText("X")
            self.bc.setText("C")
            self.bv.setText("V")
            self.bb.setText("B")
            self.bn.setText("N")
            self.bm.setText("M")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cap=0

        #Button instantiation
        self.b1.clicked.connect(lambda: self.appendcode(1))
        self.b2.clicked.connect(lambda: self.appendcode(2))
        self.b3.clicked.connect(lambda: self.appendcode(3))
        self.b4.clicked.connect(lambda: self.appendcode(4))
        self.b5.clicked.connect(lambda: self.appendcode(5))
        self.b6.clicked.connect(lambda: self.appendcode(6))
        self.b7.clicked.connect(lambda: self.appendcode(7))
        self.b8.clicked.connect(lambda: self.appendcode(8))
        self.b9.clicked.connect(lambda: self.appendcode(9))
        self.b0.clicked.connect(lambda: self.appendcode(0))
        self.bq.clicked.connect(lambda: self.appendcode('q'))
        self.bw.clicked.connect(lambda: self.appendcode('w'))
        self.be.clicked.connect(lambda: self.appendcode('e'))
        self.br.clicked.connect(lambda: self.appendcode('r'))
        self.bt.clicked.connect(lambda: self.appendcode('t'))
        self.by.clicked.connect(lambda: self.appendcode('y'))
        self.bu.clicked.connect(lambda: self.appendcode('u'))
        self.bi.clicked.connect(lambda: self.appendcode('i'))
        self.bo.clicked.connect(lambda: self.appendcode('o'))
        self.bp.clicked.connect(lambda: self.appendcode('p'))
        self.ba.clicked.connect(lambda: self.appendcode('a'))
        self.bs.clicked.connect(lambda: self.appendcode('s'))
        self.bd.clicked.connect(lambda: self.appendcode('d'))
        self.bf.clicked.connect(lambda: self.appendcode('f'))
        self.bg.clicked.connect(lambda: self.appendcode('g'))
        self.bh.clicked.connect(lambda: self.appendcode('h'))
        self.bj.clicked.connect(lambda: self.appendcode('j'))
        self.bk.clicked.connect(lambda: self.appendcode('k'))
        self.bl.clicked.connect(lambda: self.appendcode('l'))
        self.bz.clicked.connect(lambda: self.appendcode('z'))
        self.bx.clicked.connect(lambda: self.appendcode('x'))
        self.bc.clicked.connect(lambda: self.appendcode('c'))
        self.bv.clicked.connect(lambda: self.appendcode('v'))
        self.bb.clicked.connect(lambda: self.appendcode('b'))
        self.bn.clicked.connect(lambda: self.appendcode('n'))
        self.bm.clicked.connect(lambda: self.appendcode('m'))

        self.bspace.clicked.connect(lambda: self.appendcode(' '))
        self.bcap.clicked.connect(self.cap_switch)
        self.bback.clicked.connect(self.backspacecode)

#app = QApplication(sys.argv)
#name_new_user=name_new_userwindow()
#name_new_user.show()


#sys.exit(app.exec_())