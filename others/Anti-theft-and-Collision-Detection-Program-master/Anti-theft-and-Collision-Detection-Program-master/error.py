# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_error(object):
    def setupUi(self, error):
        error.setObjectName("error")
        error.resize(1095, 686)
        error.setStyleSheet("background-image: url(\'a.jpg\');")
        self.centralwidget = QtWidgets.QWidget(error)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        error.setCentralWidget(self.centralwidget)

        self.retranslateUi(error)
        QtCore.QMetaObject.connectSlotsByName(error)

    def retranslateUi(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "error"))
        self.back.setText(_translate("error", "Back to Name a New Driver"))
        self.label.setText(_translate("error", "Error Name is already exist or invalid. "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error = QtWidgets.QMainWindow()
    ui = Ui_error()
    ui.setupUi(error)
    error.show()
    sys.exit(app.exec_())

