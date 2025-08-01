from PyQt5 import QtWidgets
from adjust_fac_rec import Ui_adjust_fac_rec
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import json
import sys
# configuration
config_json='conf/conf.json'

confident_rate=0
class adjust_fac_recwindow(QtWidgets.QMainWindow,Ui_adjust_fac_rec):
    # Read conf json
    def read_json(self):
        with open(config_json, 'r') as fp:
            return json.load(fp)


    def write_json(self,file,data):
         with open(file,'w') as fp:
             json.dump(data,fp)

    #decrease
    def go_left(self):
        global confident_rate
        confident_rate-=1
        # showing confident_rate status
        self.confident_rate.setText(str(confident_rate) + '  %')

        #calling update to write to file setting
        self.update()

    #increase
    def go_right(self):
        global confident_rate
        confident_rate+=1
        # showing confident_rate status
        self.confident_rate.setText(str(confident_rate) + '  %')

        # calling update to write to file setting
        self.update()


    #Write to value to json
    def update(self):
        global confident_rate
        # load config json for speech
        my_config = self.read_json()

        my_config['confident_rate'] = str(confident_rate)

        self.write_json(config_json, my_config)


    #start here
    #read and display confident rate
    def start(self):
        global confident_rate

        # load config json for speech
        my_config = self.read_json()

        # getting speech flag for fac_rec
        confident_rate = int(my_config.get('confident_rate', ''))

        # showing confident_rate status
        self.confident_rate.setText(str(confident_rate) + '  %')



    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.left.clicked.connect(self.go_left)
        self.right.clicked.connect(self.go_right)




# app = QApplication(sys.argv)
# adjust_fac_rec=adjust_fac_recwindow()
# adjust_fac_rec.show()
# adjust_fac_rec.start()
#
#
#
# sys.exit(app.exec_())