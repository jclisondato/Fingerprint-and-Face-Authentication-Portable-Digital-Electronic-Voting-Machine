# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainmenu(object):
    def setupUi(self, mainmenu):
        mainmenu.setObjectName("mainmenu")
        mainmenu.resize(1437, 939)
        self.centralwidget = QtWidgets.QWidget(mainmenu)
        self.centralwidget.setStyleSheet("background-image: url(\'a.jpg\');")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(17)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(5, 0))
        self.label.setMaximumSize(QtCore.QSize(1000000, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(200000, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passcode_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passcode_button.sizePolicy().hasHeightForWidth())
        self.passcode_button.setSizePolicy(sizePolicy)
        self.passcode_button.setMaximumSize(QtCore.QSize(16777212, 16777215))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.passcode_button.setFont(font)
        self.passcode_button.setStyleSheet("*{color: white;\n"
"border: 5px solid red}\n"
"")
        self.passcode_button.setObjectName("passcode_button")
        self.horizontalLayout.addWidget(self.passcode_button)
        self.facial_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.facial_button.sizePolicy().hasHeightForWidth())
        self.facial_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.facial_button.setFont(font)
        self.facial_button.setStyleSheet("*{color: white;\n"
"border: 5px solid red}\n"
"")
        self.facial_button.setObjectName("facial_button")
        self.horizontalLayout.addWidget(self.facial_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        mainmenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainmenu)
        QtCore.QMetaObject.connectSlotsByName(mainmenu)

    def retranslateUi(self, mainmenu):
        _translate = QtCore.QCoreApplication.translate
        mainmenu.setWindowTitle(_translate("mainmenu", "mainmenu"))
        self.label.setText(_translate("mainmenu", "Anti-theft and Collision Detection System"))
        self.label_2.setText(_translate("mainmenu", "MAIN MENU"))
        self.passcode_button.setText(_translate("mainmenu", "PASSCODE"))
        self.facial_button.setText(_translate("mainmenu", "FACIAL RECOGNITION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainmenu = QtWidgets.QMainWindow()
    ui = Ui_mainmenu()
    ui.setupUi(mainmenu)
    mainmenu.show()
    sys.exit(app.exec_())

