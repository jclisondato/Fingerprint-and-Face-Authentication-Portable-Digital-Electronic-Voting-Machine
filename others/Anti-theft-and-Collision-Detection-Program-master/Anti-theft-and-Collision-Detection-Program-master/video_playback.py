# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_playback.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_video_playback(object):
    def setupUi(self, video_playback):
        video_playback.setObjectName("video_playback")
        video_playback.resize(1212, 765)
        video_playback.setStyleSheet(" background-image: url(\'a.jpg\');\n"
"")
        self.centralwidget = QtWidgets.QWidget(video_playback)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)
        self.widget = QVideoWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.play_button.setFont(font)
        self.play_button.setStyleSheet("color:white;\n"
"border: 3px solid red;")
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        self.time_status = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.time_status.setFont(font)
        self.time_status.setStyleSheet("color:white;")
        self.time_status.setObjectName("time_status")
        self.horizontalLayout.addWidget(self.time_status)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"background-color: white;\n"
"    border: 1px solid;\n"
"    height: 40px;\n"
"    margin: 0px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: red;\n"
"     border: 1px solid;\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"    }")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 2)
        video_playback.setCentralWidget(self.centralwidget)

        self.retranslateUi(video_playback)
        QtCore.QMetaObject.connectSlotsByName(video_playback)

    def retranslateUi(self, video_playback):
        _translate = QtCore.QCoreApplication.translate
        video_playback.setWindowTitle(_translate("video_playback", "start_car"))
        self.back_button.setText(_translate("video_playback", "Back to Review Footage"))
        self.play_button.setText(_translate("video_playback", "Pause"))
        self.time_status.setText(_translate("video_playback", "TextLabel"))


from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    video_playback = QtWidgets.QMainWindow()
    ui = Ui_video_playback()
    ui.setupUi(video_playback)
    video_playback.show()
    sys.exit(app.exec_())
