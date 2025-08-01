from PyQt5 import QtWidgets
#from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets
from change_passcode import Ui_change_passcode
from PyQt5.QtCore import QTimer
import json
import sys

from PyQt5.QtWidgets import QApplication

# configuration
config_json='conf/conf.json'

class change_passcodewindow(QtWidgets.QMainWindow,Ui_change_passcode):
    # Read conf json
    def read_json(self):
        with open(config_json, 'r') as fp:
            return json.load(fp)

    # write conf json
    def write_json(self,file,data):
        with open(file,'w') as fp:
            json.dump(data,fp)

    def backspacecode(self):
        self.lineEdit.backspace()

    def appendcode(self,n):
        self.lineEdit.insert(str(n))
        self.lineEdit.setEchoMode(2)

    # open root by comparing code
    def change_code(self):
        mydata = self.read_json()

        temp_passcode = self.lineEdit.text()
        if temp_passcode:
            mydata['my_passcode'] = temp_passcode
            self.write_json(config_json, mydata)
        else:
            pass

        if not self.timer2root.isActive():
            self.timer2root.start(20)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.change_passcode_button.clicked.connect(self.change_code)

        self.timer2root = QTimer()


        #Button instantiation
        self.Num_0.clicked.connect(lambda: self.appendcode(0))
        self.Num_1.clicked.connect(lambda: self.appendcode(1))
        self.Num_2.clicked.connect(lambda: self.appendcode(2))
        self.Num_3.clicked.connect(lambda: self.appendcode(3))
        self.Num_4.clicked.connect(lambda: self.appendcode(4))
        self.Num_5.clicked.connect(lambda: self.appendcode(5))
        self.Num_6.clicked.connect(lambda: self.appendcode(6))
        self.Num_7.clicked.connect(lambda: self.appendcode(7))
        self.Num_8.clicked.connect(lambda: self.appendcode(8))
        self.Num_9.clicked.connect(lambda: self.appendcode(9))

        self.back_button.clicked.connect(self.backspacecode)

#
# app = QApplication(sys.argv)
# change_passcode=change_passcodewindow()
# change_passcode.show()
#
# sys.exit(app.exec_())
