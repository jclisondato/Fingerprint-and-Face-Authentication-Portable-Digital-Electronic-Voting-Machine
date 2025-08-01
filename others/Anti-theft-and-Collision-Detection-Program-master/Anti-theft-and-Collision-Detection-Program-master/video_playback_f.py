from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from video_playback import Ui_video_playback
import sys
import os
import datetime
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTableWidget,QVBoxLayout,
    QTableWidgetItem, QLabel, QHBoxLayout,QGridLayout)

class video_playbackwindow(QtWidgets.QMainWindow,Ui_video_playback):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.player.setVideoOutput(self.widget)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)


        self.play_button.clicked.connect(self.play)

        self.duration=0
        self.horizontalSlider.setRange(0, 0)
        self.horizontalSlider.sliderMoved.connect(self.setPosition)


    def start(self,path):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.path.abspath(path))))
        self.player.play()
        #print(self.player.duration()+'/'+self.player.durationChanged())


    def play(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play_button.setText('Play')
        else:
            self.player.play()
            self.play_button.setText('Pause')

    def setPosition(self, position):
        self.player.setPosition(position)


    def positionChanged(self, position):
        self.time_status.setText(str(datetime.timedelta(seconds=int(position/1000))) + '/' + str(datetime.timedelta(seconds=int(self.duration/1000))))
        self.horizontalSlider.setValue(position)

    def durationChanged(self, duration):
        self.duration=duration
        self.horizontalSlider.setRange(0, duration)


#
# app = QApplication(sys.argv)
# video_playback=video_playbackwindow()
# video_playback.show()
# video_playback.start('/home/pi/Documents/6/C.mp4')
#
# sys.exit(app.exec_())