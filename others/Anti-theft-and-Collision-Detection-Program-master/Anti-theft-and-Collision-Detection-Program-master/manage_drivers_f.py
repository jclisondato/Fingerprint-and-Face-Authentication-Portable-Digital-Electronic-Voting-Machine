from PyQt5 import QtWidgets
from manage_drivers import Ui_manage_drivers
from PyQt5.QtCore import QTimer


class manage_driverswindow(QtWidgets.QMainWindow,Ui_manage_drivers):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

