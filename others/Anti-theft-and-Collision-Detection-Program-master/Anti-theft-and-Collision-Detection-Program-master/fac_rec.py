# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fac_rec.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

class Ui_fac_rec(object):
    def setupUi(self, fac_rec):
        fac_rec.setObjectName("fac_rec")
        fac_rec.resize(1289, 793)
        fac_rec.setStyleSheet("background-image: url(\'a.jpg\');")
        self.centralwidget = QtWidgets.QWidget(fac_rec)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backtomainmenu_button3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backtomainmenu_button3.sizePolicy().hasHeightForWidth())
        self.backtomainmenu_button3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.backtomainmenu_button3.setFont(font)
        self.backtomainmenu_button3.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.backtomainmenu_button3.setObjectName("backtomainmenu_button3")
        self.verticalLayout.addWidget(self.backtomainmenu_button3)
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setStyleSheet("border: 3px solid red;")
        self.camera.setObjectName("camera")
        self.verticalLayout.addWidget(self.camera)
        self.progressBar_for_camera = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_for_camera.sizePolicy().hasHeightForWidth())
        self.progressBar_for_camera.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_for_camera.setFont(font)
        self.progressBar_for_camera.setProperty("value", 24)
        self.progressBar_for_camera.setObjectName("progressBar_for_camera")
        self.verticalLayout.addWidget(self.progressBar_for_camera)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 12)
        self.verticalLayout.setStretch(2, 1)
        fac_rec.setCentralWidget(self.centralwidget)

        self.retranslateUi(fac_rec)
        QtCore.QMetaObject.connectSlotsByName(fac_rec)

        #this timer2 trigger
        self.timer_main = QTimer()

    def retranslateUi(self, fac_rec):
        _translate = QtCore.QCoreApplication.translate
        fac_rec.setWindowTitle(_translate("fac_rec", "Facial Recognition"))
        self.backtomainmenu_button3.setText(_translate("fac_rec", "Back To MainMenu"))
        self.camera.setText(_translate("fac_rec", "camera"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fac_rec = QtWidgets.QMainWindow()
    ui = Ui_fac_rec()
    ui.setupUi(fac_rec)
    fac_rec.show()
    sys.exit(app.exec_())

