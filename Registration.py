import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from PyQt5 import QtCore
import os.path, os
from PIL import Image
import numpy as np
import pickle
import re
from PyQt5.uic import loadUi
import sqlite3
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import hashlib
import face_recognition
from pyFire import votecountsPrintCSV, updateFiretoSql, voteCounts

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")



conn = sqlite3.connect('voting_database.db')
curs = conn.cursor()

class Registration(QMainWindow):
    known_face_encodings = []
    known_face_names = []

    def __init__(self):
        super(Registration, self).__init__()
        loadUi('Registrationtest.ui', self)
        self.image=None
        self.screenshot = False
        self._image_counter = 1
        self.start_webcam()
        self.fingerCapture.clicked.connect(self.fingercapture)
        self.pushCapture.clicked.connect(self.nameFirstLast)
        self.deleteButton.clicked.connect(self.deleteRow)
        self.saveButton.clicked.connect(self.save)
        self.trainButton.clicked.connect(self.trainbutton)
        self.csvexp.clicked.connect(self.csvexport)
        self.printtally.clicked.connect(self.votecounts)
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.firstNameInput.moveCursor(QTextCursor.Start)
        self.firstNameInput.setTabChangesFocus(True)
        self.lastNameInput.setTabChangesFocus(True)

    def votecounts(self):
        updateFiretoSql()
        voteCounts()
        self.warningText.setText("Done Printing")

    def csvexport(self):
        votecountsPrintCSV()
        self.warningText.setText("Done Exporting")
    def trainbutton(self):
        faceencodePKL = open('faceencode.pkl', 'wb')
        count = 0
        for root, dirs, files in os.walk(image_dir):
            count += (len(files))
        actualcount = 0
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                actualcount += 1
                print(f"{actualcount}/{count}")
                self.warningText.setText(f"{actualcount}/{count}")
                path = os.path.join(root, file)
                label = os.path.basename(root).replace("-", " ").lower()
                face_image = face_recognition.load_image_file(path)
                face_encoding = face_recognition.face_encodings(face_image)[0]
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(label)
        faceencode = []
        for name, encoded in zip(self.known_face_names, self.known_face_encodings):
            faceencode.append([name, encoded])
        pickle.dump(faceencode, faceencodePKL)
        self.warningText.setText("TRAINING DONE!!!")
        faceencodePKL.close()


    def camOtherButtons(self, y):
        self.fingerCapture.setEnabled(y)
        self.deleteButton.setEnabled(y)
        self.saveButton.setEnabled(y)
        self.trainButton.setEnabled(y)

    @QtCore.pyqtSlot()
    def start_webcam(self):
        self.capture=cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, self.image=self.capture.read()
        if self.screenshot == True:
            if self._image_counter != 200:
                firstName1 = self.firstNameInput.toPlainText().replace(" ", "").lower()
                lastName1 = self.lastNameInput.toPlainText().replace(" ", "").lower()
                fullName1 = firstName1 + ' ' + lastName1
                path = os.path.join(image_dir, fullName1)
                name = "{}.png".format(self._image_counter+1)
                print(os.path.join(path, name))
                cv2.imwrite(os.path.join(path, name), self.image)
                self._image_counter += 1
                cv2.imwrite(os.path.join(path, name), self.image)
                self.warningText.setText('Please wait! Capturing Images\n'+str(self._image_counter))
                self.camOtherButtons(False)
            else:
                self.screenshot = False
                self.saveButton.setEnabled(True)
        else:
            self.screenshot = False
            self._image_counter = 0
        self.image=cv2.flip(self.image,1)
        self.displayImage(self.image, 1)
        detected_image=self.faceDetection(self.image)
        self.displayImage(detected_image,1)

    @QtCore.pyqtSlot()
    def faceDetection(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray,1.2,minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return img

    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        outImage=outImage.rgbSwapped()

        if window==1:
            self.displayVideo.setPixmap(QPixmap.fromImage(outImage))
            self.displayVideo.setScaledContents(True)


    @QtCore.pyqtSlot()
    def nameFirstLast(self):
        firstName = self.firstNameInput.toPlainText().replace(" ", "").lower()
        lastName = self.lastNameInput.toPlainText().replace(" ", "").lower()
        fullName = firstName + ' ' + lastName

        special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if ((any(map(str.isdigit, firstName)) == True) or (special_char.search(firstName) != None)) or ((any(map(str.isdigit, lastName)) == True) or (special_char.search(lastName) != None)):
            self.warningText.setText("please don't use number/special characters")
        else:
            if os.path.exists(fullName) == False:
                os.chdir("images")
                os.makedirs(fullName)
                self.screenshot=True
            else:
                self.warningText.setText("Name Already Taken")

    @QtCore.pyqtSlot()
    def save(self):
        self.firstNameInput.setReadOnly(False)
        self.lastNameInput.setReadOnly(False)
        self.firstNameInput.clear()
        self.lastNameInput.clear()
        self.camOtherButtons(True)
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    def fingercapture(self):

        firstName = self.firstNameInput.toPlainText().replace(" ", "").lower()
        lastName = self.lastNameInput.toPlainText().replace(" ", "").lower()
        fullName = firstName + ' ' + lastName

        special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if ((any(map(str.isdigit, firstName)) == True) or (special_char.search(firstName) != None)) or (
                (any(map(str.isdigit, lastName)) == True) or (special_char.search(lastName) != None)):
            self.warningText.setText("please don't use number/special characters")
            return None
        else:
            curs.execute("SELECT name FROM voters ")

            nameList=[]
            for column in curs.fetchall():
                nameList.append(column)
            for i in range(len(nameList)):
                if fullName in nameList[i]:
                    self.warningText.setText('Name Already taken')
                    return None

        try:
            f = PyFingerprint('COM7', 57600, 0xFFFFFFFF, 0x00000000)

            if (f.verifyPassword() == False):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            self.warningText.setText('The fingerprint sensor could not be initialized!\n Exception message: ' + str(e))
            return None

            ## Gets some sensor information
            #print('Currently used templates: ' + str(f.getTemplateCount()) + '/' + str(f.getStorageCapacity()))

            ## Tries to enroll new finger
        try:
            self.warningText.setText('Waiting for finger...')

            ## Wait that finger is read
            while (f.readImage() == False):
                pass
            self.warningText.setText('Waiting for finger...')
            ## Converts read image to characteristics and stores it in charbuffer 1
            f.convertImage(0x01)

            ## Checks if finger is already enrolled
            result = f.searchTemplate()
            positionNumber = result[0]

            if (positionNumber >= 0):
                self.warningText.setText('Template already exists at position #' + str(positionNumber))
                return None

            self.warningText.setText('Remove finger')
            time.sleep(2)
            self.warningText.setText('Waiting for same finger again...')

            ## Wait that finger is read again
            while (f.readImage() == False):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 2
            f.convertImage(0x02)

            ## Compares the charbuffers
            if (f.compareCharacteristics() == 0):
                raise Exception('\nFingers do not match')

            ## Creates a template
            f.createTemplate()

            ## Saves template at new position number
            positionNumber = f.storeTemplate()
            #r = input("Enter the name = ")

            ## Loads the found template to charbuffer 1
            f.loadTemplate(positionNumber, 0x01)

            ## Downloads the characteristics of template loaded in charbuffer 1
            characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

            ## Hashes characteristics of template
            cre_hash = hashlib.sha256(characterics).hexdigest()
            #curs = conn.cursor()
            curs.execute(
                'INSERT INTO voters(name,hashval,position) values(?, ?,?)',
                (fullName, cre_hash, positionNumber))
            self.warningText.setText('Finger enrolled successfully! \n New template position #' + str(positionNumber))
            self.firstNameInput.setReadOnly(True)
            self.lastNameInput.setReadOnly(True)
            conn.commit()
            ## conn.close()

        except Exception as e:
            self.warningText.setText('Operation failed!Exception message: ' + str(e))
            return None

    def deleteRow(self):
        self.warningText.setText("")
        if self.lastNameInput.toPlainText() != "" or self.lastNameInput.toPlainText() != "" :
            try:
                f = PyFingerprint('COM7', 57600, 0xFFFFFFFF, 0x00000000)

                if (f.verifyPassword() == False):
                    raise ValueError('The given fingerprint sensor password is wrong!')

            except Exception as e:
                self.warningText.setText('The fingerprint sensor could not be initialized!\nException message: ' + str(e))
                return None

            ## Gets some sensor information
           # print('Currently used templates: ' + str(f.getTemplateCount()) + '/' + str(f.getStorageCapacity()))

            ## Tries to delete the template of the finger
            try:
                firstName = self.firstNameInput.toPlainText().replace(" ", "").lower()
                lastName = self.lastNameInput.toPlainText().replace(" ", "").lower()
                fullName = firstName + ' ' + lastName

                curs.execute("SELECT name, position FROM voters ")
                nameList = []
                print("im here")

                path = os.path.join(image_dir, fullName)
                if os.path.exists(path):
                    path = os.path.join(image_dir, fullName)
                    os.rmdir(path)
                for columns in curs.fetchall():
                    nameList.append(columns)
                for nameSql, pos in nameList:
                    if fullName in nameSql:
                        print(nameSql)
                        print(pos)
                        curs.execute('DELETE FROM voters WHERE position=? ', pos) ## delete the selected row using name
                        if (f.deleteTemplate(int(pos)) == True):
                            self.warningText.setText(nameSql + "\nfingerprint and pictures are deleted")
                            conn.commit()
                            return None

                self.warningText.setText('Name not found!')
                return None
            except Exception as e:
                print('Operation failed!')
                print('Exception message: ' + str(e))
                exit(1)
        else:
            self.warningText.setText('Please put a Name')

app=QApplication(sys.argv)
window = Registration()
window.show()
try:
    sys.exit(app.exec_())
    conn.close()
except:
    print('exiting')
    conn.close()

