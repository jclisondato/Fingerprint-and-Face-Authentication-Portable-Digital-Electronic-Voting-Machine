from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from review_footage import Ui_review_footage
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import sys
import os

import subprocess

# camera Directory
left_camera=''
right_camera=''
front_camera=''
back_camera=''




class review_footagewindow(QtWidgets.QMainWindow,Ui_review_footage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.play_left.clicked.connect(self.play_button)
        self.play_right.clicked.connect(self.play_button)
        self.play_front.clicked.connect(self.play_button)
        self.play_back.clicked.connect(self.play_button)

        self.delete_left.clicked.connect(self.delete_button)
        self.delete_right.clicked.connect(self.delete_button)
        self.delete_front.clicked.connect(self.delete_button)
        self.delete_back.clicked.connect(self.delete_button)

        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.timer_video_playback = QTimer()


        # left camera
        self.list_left.setModel(self.fileModel)

        self.list_left.clicked.connect(self.on_clicked)

        # right camera
        self.list_right.setModel(self.fileModel)

        self.list_right.clicked.connect(self.on_clicked)

        # front camera
        self.list_front.setModel(self.fileModel)

        self.list_front.clicked.connect(self.on_clicked)

        # back camera
        self.list_back.setModel(self.fileModel)

        self.list_back.clicked.connect(self.on_clicked)

        self.path = ''

        self.rescan.clicked.connect(self.rescanning)


    def rescanning(self):
        subprocess.run(["sudo", "python", "resetusb.py","Terminus"])

    def on_clicked(self, index):
        self.path = self.dirModel.fileInfo(index).absoluteFilePath()

    def play_button(self):
        if self.path=='':
            pass
        else:
            if not self.timer_video_playback.isActive():
                self.timer_video_playback.start(20)

    def delete_button(self):
        if self.path=='':
            pass
        else:
            if os.path.isfile(self.path):
                os.remove(self.path)
                self.path == ''


# app = QApplication(sys.argv)
# review_footage=review_footagewindow()
# review_footage.show()
#
# sys.exit(app.exec_())


