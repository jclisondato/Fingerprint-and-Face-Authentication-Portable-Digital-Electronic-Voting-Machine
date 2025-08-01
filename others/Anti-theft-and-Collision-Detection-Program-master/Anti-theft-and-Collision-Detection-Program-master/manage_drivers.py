# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_drivers.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_manage_drivers(object):
    def setupUi(self, manage_drivers):
        manage_drivers.setObjectName("manage_drivers")
        manage_drivers.resize(1108, 775)
        font = QtGui.QFont()
        font.setPointSize(48)
        manage_drivers.setFont(font)
        manage_drivers.setStyleSheet("background-image: url(\'a.jpg\');\n"
"")
        self.centralwidget = QtWidgets.QWidget(manage_drivers)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backtoroot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backtoroot.sizePolicy().hasHeightForWidth())
        self.backtoroot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backtoroot.setFont(font)
        self.backtoroot.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.backtoroot.setObjectName("backtoroot")
        self.verticalLayout.addWidget(self.backtoroot)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_driver = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_driver.sizePolicy().hasHeightForWidth())
        self.add_driver.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.add_driver.setFont(font)
        self.add_driver.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.add_driver.setObjectName("add_driver")
        self.horizontalLayout.addWidget(self.add_driver)
        self.remove_driver = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_driver.sizePolicy().hasHeightForWidth())
        self.remove_driver.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.remove_driver.setFont(font)
        self.remove_driver.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.remove_driver.setObjectName("remove_driver")
        self.horizontalLayout.addWidget(self.remove_driver)
        self.remove_all = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_all.sizePolicy().hasHeightForWidth())
        self.remove_all.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.remove_all.setFont(font)
        self.remove_all.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.remove_all.setObjectName("remove_all")
        self.horizontalLayout.addWidget(self.remove_all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 12)
        manage_drivers.setCentralWidget(self.centralwidget)

        self.retranslateUi(manage_drivers)
        QtCore.QMetaObject.connectSlotsByName(manage_drivers)

    def retranslateUi(self, manage_drivers):
        _translate = QtCore.QCoreApplication.translate
        manage_drivers.setWindowTitle(_translate("manage_drivers", "manage_drivers"))
        self.backtoroot.setText(_translate("manage_drivers", "Back to RootMenu"))
        self.label.setText(_translate("manage_drivers", "MANAGE DRIVERS"))
        self.add_driver.setText(_translate("manage_drivers", "Add a New Driver"))
        self.remove_driver.setText(_translate("manage_drivers", "Remove a Driver"))
        self.remove_all.setText(_translate("manage_drivers", "Remove All Drivers"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manage_drivers = QtWidgets.QMainWindow()
    ui = Ui_manage_drivers()
    ui.setupUi(manage_drivers)
    manage_drivers.show()
    sys.exit(app.exec_())
