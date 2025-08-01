from PyQt5 import QtWidgets
from error import Ui_error
#from PyQt5.QtCore import QTimer


class errorwindow(QtWidgets.QMainWindow,Ui_error):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

