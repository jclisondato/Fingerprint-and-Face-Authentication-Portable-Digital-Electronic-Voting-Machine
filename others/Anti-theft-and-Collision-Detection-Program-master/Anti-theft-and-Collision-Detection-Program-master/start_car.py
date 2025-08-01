# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_car.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_start_car(object):
    def setupUi(self, start_car):
        start_car.setObjectName("start_car")
        start_car.resize(1212, 765)
        start_car.setStyleSheet("background-image: url(\'a.jpg\');")
        self.centralwidget = QtWidgets.QWidget(start_car)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_to_root = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_to_root.sizePolicy().hasHeightForWidth())
        self.back_to_root.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_root.setFont(font)
        self.back_to_root.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.back_to_root.setObjectName("back_to_root")
        self.horizontalLayout.addWidget(self.back_to_root)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setStyleSheet("color:blue;\n"
"border: 3px solid red;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 12)
        start_car.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(start_car)
        self.statusbar.setObjectName("statusbar")
        start_car.setStatusBar(self.statusbar)

        self.retranslateUi(start_car)
        QtCore.QMetaObject.connectSlotsByName(start_car)

    def retranslateUi(self, start_car):
        _translate = QtCore.QCoreApplication.translate
        start_car.setWindowTitle(_translate("start_car", "start_car"))
        self.back_to_root.setText(_translate("start_car", "Back to RootMenu"))
        self.label.setText(_translate("start_car", "Start the car now !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start_car = QtWidgets.QMainWindow()
    ui = Ui_start_car()
    ui.setupUi(start_car)
    start_car.show()
    sys.exit(app.exec_())

