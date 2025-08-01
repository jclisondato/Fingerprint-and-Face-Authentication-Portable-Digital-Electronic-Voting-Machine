from PyQt5 import QtWidgets
from passcode import Ui_passcode
from PyQt5.QtCore import QTimer,QThread
import json
import subprocess
from PyQt5.QtWidgets import QApplication
import sys
# speech feature
from gtts import gTTS

# configuration
config_json='conf/conf.json'
speech=0


class Mythread(QThread):
    def run(self):
        subprocess.run(["mpg123", "-q", "welcomeback.mp3"])

class passcodewindow(QtWidgets.QMainWindow,Ui_passcode):

    # Read conf json
    def read_json(self):
        with open(config_json, 'r') as fp:
            return json.load(fp)

    def backspacecode(self):
        self.lineEdit.backspace()

    def appendcode(self,n):
        self.lineEdit.insert(str(n))
        self.lineEdit.setEchoMode(2)

    # open root by comparing code
    def compare_code(self):
        global speech
        temp_passcode = self.lineEdit.text()

        # load config json for speech
        my_config = self.read_json()

        # getting speech flag for fac_rec
        speech=int(my_config.get('speech', ''))
        default_passcode = my_config.get('default_passcode', '')
        my_passcode = my_config.get('my_passcode', '')

        if my_passcode == temp_passcode or default_passcode==temp_passcode:
            if speech:
                thread = Mythread(self)
                thread.start()
            if not self.timer2root.isActive():
                self.timer2root.start(20)
        else:
            if not self.timer2main.isActive():
                self.timer2main.start(20)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.enter_button.clicked.connect(self.compare_code)

        self.timer2root = QTimer()
        self.timer2main = QTimer()

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
# passcode=passcodewindow()
# passcode.show()
#
# sys.exit(app.exec_())
#
