#SPEECH
#from gtts import gTTS
#import os
# tts = gTTS(text='Please come close to the camera until you see the red rectangle, and remain still for capturing', lang='en')
# tts.save("cap_new_driver_no.mp3")
# os.system("mpg123 -q cap_new_driver_no.mp3")


# CHECK INTERNET
# import socket
# REMOTE_SERVER = "www.google.com"
# def is_connected():
#   try:
#     host = socket.gethostbyname(REMOTE_SERVER)
#     s = socket.create_connection((host, 80), 2)
#     return True
#   except:
#      pass
#   return False
# print(is_connected())
#
# Write json
# import json
# def write(file,data):
#     with open(file,'w') as fp:
#         json.dump(data,fp)
#
# file_name='conf/conf.json'
#
# data = {}
# data['speech'] = '1'
# data['default_passcode'] = '1111'
# data['my_passcode'] = '2222'
# write(file_name,data)
#
# Read json
# import json
# def read_json(file):
#     with open(file,'r') as fp :
#         return json.load(fp)
#
# mydata=read('conf/conf.json')
# print(mydata.get('password',''))

# PyQt5 Video player
#!/usr/bin/env python

#sudo apt-get install libqt5multimedia5-plugins

# import os
# from PyQt5.QtCore import QDir, Qt, QUrl
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
#         QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
# from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
# from PyQt5.QtGui import QIcon
# import sys
#
# class VideoWindow(QMainWindow):
#
#     def __init__(self, parent=None):
#         super(VideoWindow, self).__init__(parent)
#         self.setWindowTitle("PyQt Video Player Widget Example - pythonprogramminglanguage.com")
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#
#         videoWidget = QVideoWidget()
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.errorLabel = QLabel()
#         self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
#                 QSizePolicy.Maximum)
#
#
#
#         # Create a widget for window contents
#         wid = QWidget(self)
#         self.setCentralWidget(wid)
#
#         # Create layouts to place inside widget
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.errorLabel)
#
#
#         # Set widget to contain window contents
#         wid.setLayout(layout)
#
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#
#     def openFile(self):
#         self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile((os.path.abspath("/home/pi/Documents/6/C.mp4")))))
#         self.playButton.setEnabled(True)
#
#         #if fileName != '':
#         #    self.mediaPlayer.setMedia(
#         #            QMediaContent(QUrl.fromLocalFile(fileName)))
#         #    self.playButton.setEnabled(True)
#
#     def play(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#         else:
#             self.mediaPlayer.play()
#
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     player = VideoWindow()
#     player.resize(640, 480)
#     player.showFullScreen()
#     player.openFile()
#     sys.exit(app.exec_())
# #
#
# import sys
# import os
# from PyQt5 import QtGui, QtCore
# from PyQt5.QtCore import QDir, Qt, QUrl
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTableWidget,QVBoxLayout,
#     QTableWidgetItem, QLabel, QHBoxLayout,QGridLayout)

# class Window(QWidget):
#     def __init__(self,):
#         super().__init__()
#         self.VideoWidget = QVideoWidget()
#
#         self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(os.path.abspath("/home/pi/Documents/6/C.mp4"))))
#         self.player.play()
#         self.player.setVideoOutput(self.VideoWidget)
#
#         self.layout = QHBoxLayout()
#         self.layout.addWidget(self.VideoWidget)
#
#         self.setLayout(self.layout)
#
#         self.move(0,0)
#         self.resize(320, 240)
#
#         self.show()
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     app.exec_()
# import sys
#
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
#
#
# import sys
# import os
# from PyQt5 import QtGui, QtCore
# from PyQt5.QtCore import QDir, Qt, QUrl
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTableWidget,QVBoxLayout,
#     QTableWidgetItem, QLabel, QHBoxLayout,QGridLayout)
#
# class Widget(QWidget):
#     def __init__(self, *args, **kwargs):
#         QWidget.__init__(self, *args, **kwargs)
#         hlay = QHBoxLayout(self)
#         #self.treeview = QTreeView()
#         self.listview = QListView()
#         #hlay.addWidget(self.treeview)
#         hlay.addWidget(self.listview)
#
#         path = QDir.rootPath()
#         print(path)
#         #self.dirModel = QFileSystemModel()
#         #self.dirModel.setRootPath(QDir.rootPath())
#         #self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
#
#         self.fileModel = QFileSystemModel()
#         self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)
#
#         #self.treeview.setModel(self.dirModel)
#         self.listview.setModel(self.fileModel)
#
#         #self.treeview.setRootIndex(self.dirModel.index('/home/phong/Desktop/antitheft/GUI/'))
#         self.listview.setRootIndex(self.fileModel.index(path))
#
#         #self.treeview.clicked.connect(self.on_clicked)
#
#         self.listview.setRootIndex(self.fileModel.setRootPath('/home/phong/Desktop/antitheft/GUI/6'))
#     def on_clicked(self, index):
#         path = self.dirModel.fileInfo(index).absoluteFilePath()
#         self.listview.setRootIndex(self.fileModel.setRootPath(path))
#         print(path)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = Widget()
#     w.show()
#     sys.exit(app.exec_())
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#
# class Widget(QWidget):
#     def __init__(self, *args, **kwargs):
#         QWidget.__init__(self, *args, **kwargs)
#         hlay = QHBoxLayout(self)
#         self.treeview = QTreeView()
#         self.listview = QListView()
#         hlay.addWidget(self.treeview)
#         hlay.addWidget(self.listview)
#
#         path = QDir.rootPath()
#
#         self.dirModel = QFileSystemModel()
#         self.dirModel.setRootPath(QDir.rootPath())
#         self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
#
#         self.fileModel = QFileSystemModel()
#         self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)
#
#         self.treeview.setModel(self.dirModel)
#         self.listview.setModel(self.fileModel)
#
#         self.treeview.setRootIndex(self.dirModel.index(path))
#         self.listview.setRootIndex(self.fileModel.index(path))
#
#         self.treeview.clicked.connect(self.on_clicked)
#
#     def on_clicked(self, index):
#         path = self.dirModel.fileInfo(index).absoluteFilePath()
#         self.listview.setRootIndex(self.fileModel.setRootPath(path))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = Widget()
#     w.show()
#     sys.exit(app.exec_())
import subprocess
# subprocess.run(["umount","/dev/sda1"])
import datetime
time_now=datetime.datetime.now()
update_time=str(time_now.year)+str(time_now.month).zfill(2)+str(time_now.day).zfill(2)+str(time_now.hour).zfill(2)+str(time_now.hour).zfill(2)+str(time_now.minute).zfill(2)+str(time_now.second).zfill(2)+' '+'Y'
print(update_time)