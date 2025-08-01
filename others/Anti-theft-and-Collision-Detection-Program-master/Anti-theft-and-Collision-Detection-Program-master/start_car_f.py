from PyQt5 import QtWidgets
from start_car import Ui_start_car

class start_carwindow(QtWidgets.QMainWindow,Ui_start_car):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

