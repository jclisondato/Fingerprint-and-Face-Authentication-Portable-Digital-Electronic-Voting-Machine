# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_trainer(object):
    def setupUi(self, trainer):
        trainer.setObjectName("trainer")
        trainer.resize(1098, 699)
        trainer.setStyleSheet("background-image: url(\'a.jpg\');\n"
"")
        self.centralwidget = QtWidgets.QWidget(trainer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.pictures_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictures_info.sizePolicy().hasHeightForWidth())
        self.pictures_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pictures_info.setFont(font)
        self.pictures_info.setStyleSheet("color: white;\n"
"border: 3px solid red;")
        self.pictures_info.setObjectName("pictures_info")
        self.verticalLayout.addWidget(self.pictures_info)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        trainer.setCentralWidget(self.centralwidget)

        self.retranslateUi(trainer)
        QtCore.QMetaObject.connectSlotsByName(trainer)

    def retranslateUi(self, trainer):
        _translate = QtCore.QCoreApplication.translate
        trainer.setWindowTitle(_translate("trainer", "trainer"))
        self.label.setText(_translate("trainer", "Processing Drivers"))
        self.pictures_info.setText(_translate("trainer", "pictures Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    trainer = QtWidgets.QMainWindow()
    ui = Ui_trainer()
    ui.setupUi(trainer)
    trainer.show()
    sys.exit(app.exec_())

