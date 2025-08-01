from PyQt5 import QtWidgets
from mainmenu import Ui_mainmenu


class mainmenuwindow(QtWidgets.QMainWindow,Ui_mainmenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

