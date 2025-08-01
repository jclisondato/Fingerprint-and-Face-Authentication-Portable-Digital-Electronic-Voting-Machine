from PyQt5 import QtWidgets
from error_fac_rec import Ui_error_fac_rec
from PyQt5.QtCore import QTimer


class error_fac_recwindow(QtWidgets.QMainWindow,Ui_error_fac_rec):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


