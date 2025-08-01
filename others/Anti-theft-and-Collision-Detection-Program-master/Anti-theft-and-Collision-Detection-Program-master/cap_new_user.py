# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cap_new_user.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cap_new_user(object):
    def setupUi(self, cap_new_user):
        cap_new_user.setObjectName("cap_new_user")
        cap_new_user.resize(1177, 761)
        cap_new_user.setStyleSheet("background-image: url(\'a.jpg\');")
        self.centralwidget = QtWidgets.QWidget(cap_new_user)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.camera.setObjectName("camera")
        self.horizontalLayout.addWidget(self.camera)
        self.horizontalLayout.setStretch(0, 6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.start.setObjectName("start")
        self.verticalLayout_2.addWidget(self.start)
        self.verticalLayout_2.setStretch(1, 7)
        self.verticalLayout_2.setStretch(3, 1)
        cap_new_user.setCentralWidget(self.centralwidget)

        self.retranslateUi(cap_new_user)
        QtCore.QMetaObject.connectSlotsByName(cap_new_user)

    def retranslateUi(self, cap_new_user):
        _translate = QtCore.QCoreApplication.translate
        cap_new_user.setWindowTitle(_translate("cap_new_user", "cap_new_user"))
        self.label_3.setText(_translate("cap_new_user", "Capture a new driver"))
        self.camera.setText(_translate("cap_new_user", "camera"))
        self.start.setText(_translate("cap_new_user", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cap_new_user = QtWidgets.QMainWindow()
    ui = Ui_cap_new_user()
    ui.setupUi(cap_new_user)
    cap_new_user.show()
    sys.exit(app.exec_())

