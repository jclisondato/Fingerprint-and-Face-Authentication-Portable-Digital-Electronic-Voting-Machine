# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'security.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_security(object):
    def setupUi(self, security):
        security.setObjectName("security")
        security.resize(1212, 658)
        security.setStyleSheet(" background-image: url(\'a.jpg\');\n"
"")
        self.centralwidget = QtWidgets.QWidget(security)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addWidget(self.back_to_root)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.adjust_threshold = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adjust_threshold.sizePolicy().hasHeightForWidth())
        self.adjust_threshold.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.adjust_threshold.setFont(font)
        self.adjust_threshold.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.adjust_threshold.setObjectName("adjust_threshold")
        self.horizontalLayout.addWidget(self.adjust_threshold)
        self.change_passcode = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_passcode.sizePolicy().hasHeightForWidth())
        self.change_passcode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.change_passcode.setFont(font)
        self.change_passcode.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.change_passcode.setObjectName("change_passcode")
        self.horizontalLayout.addWidget(self.change_passcode)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 6)
        security.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(security)
        self.statusbar.setObjectName("statusbar")
        security.setStatusBar(self.statusbar)

        self.retranslateUi(security)
        QtCore.QMetaObject.connectSlotsByName(security)

    def retranslateUi(self, security):
        _translate = QtCore.QCoreApplication.translate
        security.setWindowTitle(_translate("security", "security"))
        self.back_to_root.setText(_translate("security", "Back to RootMenu"))
        self.label.setText(_translate("security", "SECURITY"))
        self.adjust_threshold.setText(_translate("security", "Adjust Threshold"))
        self.change_passcode.setText(_translate("security", "Change Passcode"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    security = QtWidgets.QMainWindow()
    ui = Ui_security()
    ui.setupUi(security)
    security.show()
    sys.exit(app.exec_())
