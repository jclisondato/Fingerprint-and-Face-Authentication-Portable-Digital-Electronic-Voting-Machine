import os.path
import cv2
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import sys
from cap_new_user import Ui_cap_new_user

from imutils.video import VideoStream
import subprocess
import time
import imutils
# speech feature
from gtts import gTTS
import socket
REMOTE_SERVER = "www.google.com"

#save.txt
save_path='save.txt'

#Intel Haarcascade file
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#for trainning xml file
recognizer = cv2.face.LBPHFaceRecognizer_create()

#path to dataset
dataset_path=('dataset/')


#path to yml
yml_path=('trainer/trainer.yml')

#font
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize amount of number to take for training
sample_number = 10
counter=0
first=0
complete = 0
cap_in=0
g_name=' '
speech=0
speak=0


def check_internet():
  try:
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False


class Mythread(QThread):
    def run(self):
        global speech, g_name,speak
        if speech and speak==0:
            speak=1
            if check_internet() and g_name != ' ':
                tts = gTTS(text= str(g_name) +'. Please come close to the camera until you see the red rectangle, and remain still for capturing '+ '!', lang='en')
                tts.save("cap_new_driver.mp3")
                subprocess.run(["mpg123", "-q", "cap_new_driver.mp3"])
            else:
                subprocess.run(["mpg123", "-q", "cap_new_driver_no.mp3"])
        else:
            pass


class cap_new_userwindow(QtWidgets.QMainWindow,Ui_cap_new_user):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.speech=1
        self.new_name=' '

        # create a timer

        #this timer will go to start video loop
        self.timer = QTimer()

        #this timer will start to take picture
        self.timer2 = QTimer()

        #this timer to get to next window
        self.timer3 = QTimer()
        self.Id=0

        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.timer2.timeout.connect(self.take_sample)

        #button for start capture
        self.start.clicked.connect(self.take_pic)

    def take_pic(self):
        global first
        if not first:
            first=1
            p = self.qImg
            p.save('preview/'+str(self.Id), 'png')
        if not self.timer2.isActive():
            self.timer2.start(1000)


    # ================================Fac_Rec==================================
    def camera_init(self):
        global sample_number, complete,first,g_name,speech,first
        self.cap = VideoStream(usePiCamera=1).start()
        time.sleep(2.0)
        first = 0

        g_name=self.new_name
        speech=self.speech


        self.roi_gray = 0
        self.progressBar.setValue(0)

        # if timer is stopped and read_yml is valid
        if not self.timer.isActive():
            # start timer
            self.timer.start(20)

    def take_sample(self):
        global counter,sample_number,cap_in,first
        Id=self.Id

        if counter != sample_number and cap_in == 1:
            cap_in=0
            counter += 1
            self.progressBar.setValue(counter * (100 / sample_number))
            # storing the driver face in the dataset folder as jpg
            cv2.imwrite("dataset/User." + str(Id) + "." + str(counter) + ".jpg",self.roi_gray,[int(cv2.IMWRITE_JPEG_QUALITY), 100])

        # done taking sample clean up and call trainer xml
        elif counter == sample_number:
            self.timer.stop()
            self.timer2.stop()
            # release video capture
            self.cap.stop()

            # reset values for next time
            first = 0
            counter = 0

            # timer start back to manage
            if not self.timer3.isActive():
                # start timer
                self.timer3.start(20)
        else:
            pass



    def viewCam(self):
        global sample_number, first,counter, cap_in,speak
        Id=1
        if self.timer.isActive():
            # read image in BGR format
            image = self.cap.read()
            if image is not None:

                # convert image to RGB format
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                #if first:
                # ======================================================================================
                # turn image into gray
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # start to detect faces
                faces = detector.detectMultiScale(gray, 1.3, 5)


                 # start drawing a rectangle for faces
                for (x, y, w, h) in faces:
                    #print(x,y,w,h)
                    #if w>200 and h>200:
                    if w>200:
                        cap_in=1
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        self.roi_gray = gray[y:y + h, x:x + w]
                    elif self.speech and speak==0:
                        thread = Mythread(self)
                        thread.start()
                    # ====================================================================================

                image = imutils.resize(image, width=500)
                # get image infos
                height, width, channel = image.shape
                step = channel * width

                # create QImage from image
                self.qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
                # show image in img_label
                self.camera.setScaledContents(True)
                self.camera.setPixmap(QPixmap.fromImage(self.qImg))
            else:
                pass

        else:
            pass

# app = QApplication(sys.argv)
# cap_new_user=cap_new_userwindow()
# cap_new_user.show()
# cap_new_user.camera_init()
#
# sys.exit(app.exec_())
#
#
#
#
#





















