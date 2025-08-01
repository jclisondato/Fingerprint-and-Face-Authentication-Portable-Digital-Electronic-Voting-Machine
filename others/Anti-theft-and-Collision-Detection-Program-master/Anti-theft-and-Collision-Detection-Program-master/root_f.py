from PyQt5 import QtWidgets
from root import Ui_root
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import json
import sys
# configuration
config_json='conf/conf.json'

class rootwindow(QtWidgets.QMainWindow,Ui_root):
    # Read conf json
    def read_json(self):
        with open(config_json, 'r') as fp:
            return json.load(fp)


    def write_json(self,file,data):
         with open(file,'w') as fp:
             json.dump(data,fp)


    def change_speech(self):
        # load config json for speech
        my_config = self.read_json()

        # getting speech flag for fac_rec
        speech = int(my_config.get('speech', ''))
        if speech:
            speech='off'
            my_config['speech'] = '0'

        else:
            speech='on'
            my_config['speech'] = '1'
        # showing speech status
        self.speech_button.setText('Speech:\n' + speech)
        self.write_json(config_json,my_config)


    def start(self):
        # load config json for speech
        my_config = self.read_json()

        # getting speech flag for fac_rec
        speech = int(my_config.get('speech', ''))
        if speech:
            speech='on'
        else:
            speech='off'

        # showing speech status
        self.speech_button.setText('Speech:\n'+ speech)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.speech_button.clicked.connect(self.change_speech)



# app = QApplication(sys.argv)
# root=rootwindow()
# root.show()
# root.start()
#
#
# sys.exit(app.exec_())