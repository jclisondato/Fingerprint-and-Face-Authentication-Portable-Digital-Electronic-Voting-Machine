from PyQt5 import QtWidgets
from security import Ui_security

class securitywindow(QtWidgets.QMainWindow,Ui_security):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

