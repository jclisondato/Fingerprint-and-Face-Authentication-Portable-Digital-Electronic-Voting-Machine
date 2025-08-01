from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
import face_recognition
import os, sys
import cv2
import numpy as np
import math
import pickle

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


class Recognition(QMainWindow):
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True

    def encode_faces(self):
        faceencodePKL = open('faceencode.pkl', 'rb')
        faceencodeloop = pickle.load(faceencodePKL)
        for label,face_encoding in faceencodeloop:
            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(label)

    def __init__(self):
        super(Recognition, self).__init__()
        loadUi('faceRECOGNITIONWINDOW.ui', self)
        #self.encode_faces()
        self.start_webcam()
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    def start_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)
        self.displayImage(self.image, self.known_face_encodings,self.known_face_names, 1)
        #detected_image = self.faceDetection(self.image)

    @QtCore.pyqtSlot()
    # def faceDetection(self, img):
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     faces = self.face_cascade.detectMultiScale(gray, 1.2, minNeighbors=5)
    #     for (x, y, w, h) in faces:
    #         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #
    #     return img

    def displayImage(self, img,known_face_encodings,known_face_names, window=1):
        try:
            img = self.face_rec(img, known_face_encodings,known_face_names)
        except Exception as e:
            print(e)
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.webcam.setPixmap(QPixmap.fromImage(outImage))
            self.webcam.setScaledContents(True)


    def face_rec(self, frame, known_face_encodings, known_face_names):
            # Only process every other frame of video to save time
            if self.process_current_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                # Find all the faces and face encodings in the current frame of video
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    confidence = '???'

                    # Calculate the shortest distance to face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                        confidence = face_confidence(face_distances[best_match_index])

                    self.face_names.append(f'{name} ({confidence})')

            # Display the results
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Create the frame with the name
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)
            return frame

app=QApplication(sys.argv)
window = Recognition()
window.show()
try:
    sys.exit(app.exec_())
    conn.close()
except:
    print('exiting')
    conn.close()