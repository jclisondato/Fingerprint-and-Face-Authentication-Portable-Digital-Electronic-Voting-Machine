from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer
import face_recognition
import os, sys
import cv2
import numpy as np
import math
import pickle
from PyQt5 import QtWidgets
#from eye_blink_detection import blink
from eye_blink_detection1 import call


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")


# Helper
def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'

rec2blink = []
nameget = []
class Recognition(QMainWindow):
    def __init__(self):
        super(Recognition, self).__init__()
        loadUi("faceRECOGNITIONWINDOW.ui", self)
        self.startVideo()
        self.image = None
        self.opencam.clicked.connect(self.changeBlink)

    @pyqtSlot()
    def startVideo(self):
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)  # Create Timer
        self.class_names = []
        self.encode_list = []
        faceencodePKL = open('faceencode.pkl', 'rb')
        faceencodeloop = pickle.load(faceencodePKL)
        for label, face_encoding in faceencodeloop:
            self.encode_list.append(face_encoding)
            self.class_names.append(label)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)
        # if self.changeBlink() == 1:
        #     self.timer.timeout.connect(self.update_frame())
        # else:
        #     self.timer.timeout.connect(self.update_frame())

    def changeBlink(self):
        rec2blink.append(True)

    def face_rec_(self, frame, encode_list_known, class_names):

        # face recognition
        faces_cur_frame = face_recognition.face_locations(frame)
        encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)
        # count = 0
        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)

            if widget.currentIndex() == 0:
                #nameget.clear()
                best_match_index = np.argmin(face_dis)
                # print("s",best_match_index)
                name = "unknown"
                if match[best_match_index]:
                    name = class_names[best_match_index].lower()
                    y1, x2, y2, x1 = faceLoc
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    #cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                    #cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    if len(nameget) != 1:
                        nameget.append(name)
                    elif nameget[0] != name:
                        nameget.clear()
                        nameget.append(name)
                    print(nameget)
                    self.namePrev.setText(f"Are you?\n\n{name}")
                else:
                    name = "Unknown"
                    y1, x2, y2, x1 = faceLoc
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    #cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    self.namePrev.setText(name)

        return frame

    def update_frame(self):
        ret, self.image = self.capture.read()
        if True in rec2blink:
            call()
            print(call())

        else:
            self.displayImage(self.image, self.encode_list, self.class_names, 1)

    def displayImage(self, image, encode_list, class_names, window=1):

        image = cv2.resize(image, (640, 480))
        try:
            image = self.face_rec_(image, encode_list, class_names)
        except Exception as e:
            print(e)
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.webcam.setPixmap(QPixmap.fromImage(outImage))
            self.webcam.setScaledContents(True)




app=QApplication(sys.argv)
window = Recognition()

widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
#widget.addWidget(window2)
window.setFixedWidth(800)
window.setFixedHeight(480)
widget.show()
try:
    sys.exit(app.exec_())
    conn.close()
except:
    print('exiting')
    conn.close()