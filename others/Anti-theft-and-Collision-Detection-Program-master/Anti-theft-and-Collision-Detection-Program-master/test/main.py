import os
import sys

from PyQt5 import QtWidgets, QtMultimedia, uic, QtCore

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi(os.path.join('/home/pi/Documents/6/test/form.ui'),self)
        self.player = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        file = '/home/pi/Documents/6/test/small.mp4'
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file)))
        self.player.setVideoOutput(self.ui.widget)
        self.player.play()
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())
