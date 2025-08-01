# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_fac_rec.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_error_fac_rec(object):
    def setupUi(self, error_fac_rec):
        error_fac_rec.setObjectName("error_fac_rec")
        error_fac_rec.resize(1190, 757)
        error_fac_rec.setStyleSheet("background-image: url(\'a.jpg\');")
        self.centralwidget = QtWidgets.QWidget(error_fac_rec)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        error_fac_rec.setCentralWidget(self.centralwidget)

        self.retranslateUi(error_fac_rec)
        QtCore.QMetaObject.connectSlotsByName(error_fac_rec)

    def retranslateUi(self, error_fac_rec):
        _translate = QtCore.QCoreApplication.translate
        error_fac_rec.setWindowTitle(_translate("error_fac_rec", "error_fac_rec"))
        self.pushButton.setText(_translate("error_fac_rec", "Back to MainMenu"))
        self.label.setText(_translate("error_fac_rec", "Please add a driver before using this feature !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error_fac_rec = QtWidgets.QMainWindow()
    ui = Ui_error_fac_rec()
    ui.setupUi(error_fac_rec)
    error_fac_rec.show()
    sys.exit(app.exec_())

