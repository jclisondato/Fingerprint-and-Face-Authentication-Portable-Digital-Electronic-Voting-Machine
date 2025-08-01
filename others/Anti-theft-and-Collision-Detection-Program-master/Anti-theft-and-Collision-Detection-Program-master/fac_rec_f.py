import os.path
from PyQt5.QtCore import QThread
from fac_rec import Ui_fac_rec
from PyQt5.QtWidgets import QApplication
from imutils.video import VideoStream
#import face_recognition
import imutils
import pickle
import time
import sys
# speech feature
from gtts import gTTS
import socket
REMOTE_SERVER = "www.google.com"
import subprocess

#+=============================
import os.path
import cv2
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from fac_rec import Ui_fac_rec
import json
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


confirm_face=2
unlock_root=0
unlock_frame = 0
read_yml = 0
name_array = []

# import Opencv module
encoder_data = 0
speech=0
g_name=0
confident_rate=0
# configuration
config_json='conf/conf.json'

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
        global speech, g_name
        if speech:
            if check_internet() and g_name!=' ':
                tts = gTTS(text='Welcome back '+g_name + '!', lang='en')
                tts.save("welcomeback_driver.mp3")
                subprocess.run(["mpg123", "-q", "welcomeback_driver.mp3"])
            else:
                subprocess.run(["mpg123", "-q", "welcomeback.mp3"])
        else:
            pass


class fac_recwindow(QtWidgets.QMainWindow,Ui_fac_rec):
    # Read conf json
    def read_json(self):
        with open(config_json, 'r') as fp:
            return json.load(fp)


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # create a timer
        self.timer = QTimer()
        self.speech = 1

    # ================================Fac_Rec==================================
    def camera_init(self):
        global read_yml, name_array, unlock_root, confirm_face, unlock_frame,speech, confident_rate
        self.cap = VideoStream(usePiCamera=1).start()
        time.sleep(2.0)
        speech=self.speech

        # load config json for speech
        my_config = self.read_json()

        # getting confident_rate for fac_rec
        confident_rate = int(my_config.get('confident_rate', ''))




        # =============================================================================================================

        # how many frame would it take to unclock the car
        unlock_frame = 0
        # condition start dash cam if exist yml file
        read_yml = 0
        # Array to store the name
        name_array = []
        # unlock_root condition to go to root
        unlock_root = 0
        # open save.txt
        if os.path.isfile(save_path):
            with open(save_path, 'r+') as my_file:
                name_array = my_file.readlines()
        # if name_array is not empty
        if name_array:
            # Read trainer.yml
            if os.path.isfile(yml_path):
                # read the trainer.yml file
                recognizer.read(yml_path)
                read_yml = 1
            else:
                # GUI
                print('Error yml file')
        else:
            print('Error name_array is empty')
        # ==============================================================================================================

        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # if timer is stopped and read_yml is valid
        #if not self.timer.isActive() and read_yml == 1 and self.cap.isOpened():
        if not self.timer.isActive():
            # start timer
            self.timer.start(10)



    def viewCam(self):
        global unlock_frame,read_yml,name_array,g_name, speech, confident_rate
        if self.timer.isActive():
            # read image in BGR format
            image = self.cap.read()
            if image is not None:
                # convert image to RGB format
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # ======================================================================================
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.2, 5)

                for (x, y, w, h) in faces:
                    if w>200:
                        #print(x,y,w,h)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (225, 0, 0), 2)
                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if (conf < (100-confident_rate)):
                            # increment unlock_frame
                            unlock_frame += 1
                            # get id to name according to name list
                            # Bug here Check Id before getting the name_array
                            if Id > 0 and Id <= len(name_array):
                                Id = name_array[Id - 1][:-1]
                            else:
                                Id=' '
                            conf = "  {0}%".format(round(100 - conf))

                            # confirm face
                            if unlock_frame == confirm_face:
                                unlock_frame += 1
                                g_name=str(Id)
                                # stop timer
                                self.timer.stop()
                                # release video capture
                                self.cap.stop()

                                #start speech
                                if speech:
                                    thread = Mythread(self)
                                    thread.start()

                                if not self.timer_main.isActive():
                                    self.timer_main.start(20)
                        else:
                            Id = "Unknown"
                            conf = "  {0}%".format(round(100 - conf))
                        cv2.putText(image, str(conf), (x + 150, y + h - 5), font, 1, (0, 0, 255), 3)
                        cv2.putText(image, str(Id), (x, y + h), font, 1, (0, 255, 0), 3)

                    # ======================================================================================
                    else:
                         pass
                self.progressBar_for_camera.setValue(unlock_frame * (100 / confirm_face))
                # get image infos
                image = imutils.resize(image, width=500)
                height, width, channel = image.shape
                step = channel * width
                # create QImage from image
                qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
                # show image in img_label
                self.camera.setScaledContents(True)
                self.camera.setPixmap(QPixmap.fromImage(qImg))
            else:
                pass
        else:
            pass





#
# app = QApplication(sys.argv)
# fac_rec=fac_recwindow()
# fac_rec.show()
# fac_rec.camera_init()
#
# sys.exit(app.exec_())
