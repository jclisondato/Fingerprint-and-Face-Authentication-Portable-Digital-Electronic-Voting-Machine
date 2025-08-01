
from trainer import Ui_trainer
import os.path
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal,QTimer
import numpy as np
from PIL import Image
import cv2
import os


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

# grab the paths to the input images in our dataset
dataset='dataset/'

encoder = 'trainer/encodings.pickle'

total=0
knownEncodings = []
knownNames = []


class Mythread(QThread):
    #initializing signals
    change_value = pyqtSignal(int)
    #driver_info = pyqtSignal(str)
    # Trainer produce trainer.yml for exam_face
    def run(self):

        def trainer_xml(path):
            global total
            image_counter=0
            # get the path of all the files in the folder
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            # create empth face list
            faceSamples = []
            # create empty ID list
            Ids = []

            total=len(imagePaths)
            # now looping through all the image paths and loading the Ids and the images
            for imagePath in imagePaths:
                image_counter+=1
                #print(image_counter)
                self.change_value.emit(image_counter)

                # Updates in Code
                # ignore if the file does not have jpg extension :
                if (os.path.split(imagePath)[-1].split(".")[-1] != 'jpg'):
                    continue

                # loading the image and converting it to gray scale
                pilImage = Image.open(imagePath).convert('L')

                # Now we are converting the PIL image into numpy array
                imageNp = np.array(pilImage, 'uint8')
                # getting the Id from the image
                Id = int(os.path.split(imagePath)[-1].split(".")[1])
                # extract the face from the training image sample
                faces = detector.detectMultiScale(imageNp)
                # If a face is there then append that in the list as well as Id of it
                for (x, y, w, h) in faces:
                    faceSamples.append(imageNp[y:y + h, x:x + w])
                    Ids.append(Id)


            return faceSamples, Ids

        faces, Ids = trainer_xml(dataset_path)
        recognizer.train(faces, np.array(Ids))
        recognizer.save(yml_path)

        # value to start timer get back
        image_counter = -1
        self.change_value.emit(image_counter)


class trainerwindow(QtWidgets.QMainWindow,Ui_trainer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)

        self.timer_back2root = QTimer()



    def start(self):
        # display current works

        #start threading
        self.thread=Mythread(self)
        self.thread.change_value.connect(self.set_val)
        self.thread.start()






    def set_val(self,val):
        if val==-1:
            #print('get back to root')
            if not self.timer_back2root.isActive():
                # start timer
                self.timer_back2root.start(20)
        else:
            # set progress bar
            self.progressBar.setValue((val + 1) * (100 / total))
            self.pictures_info.setText('processing image:   ' + str(val + 1) +' / '+ str(total))
            if val==total:
                self.pictures_info.setText('saving file to the system')






#
# app = QApplication(sys.argv)
# trainer=trainerwindow()
# trainer.show()
# trainer.start()
#
#
# sys.exit(app.exec_())
