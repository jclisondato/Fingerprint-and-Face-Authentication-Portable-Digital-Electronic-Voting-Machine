from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSlot, QTimer
import face_recognition
import os, sys
import cv2
import numpy as np
import math
import pickle
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3
from pyfingerprint.pyfingerprint import PyFingerprint
from PyQt5 import QtWidgets
from pyFire import *

from eye_blink_detection1 import call
#from printertest import printcandidates
#################################################################################################
##Initialize
conn = sqlite3.connect('voting_database.db')
curs = conn.cursor()

f = PyFingerprint('COM7', 57600, 0xFFFFFFFF, 0x00000000)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'


############################################################################
class Voting(QMainWindow):
    def __init__(self, parent = None):
        super(Voting, self).__init__(parent)
        loadUi('votersGui1.ui', self)
        updateFiretoSql()
        self.initFinger.clicked.connect(self.finger)

    def finger(self):
        while (f.readImage() == False):
            pass
        self.putFinger()

    def putFinger(self):
        # try:
        #     # print("\nscan the finger print of student for getting info. from database \n")
        #     f = PyFingerprint('COM7', 57600, 0xFFFFFFFF, 0x00000000)
        #
        #     if (f.verifyPassword() == False):
        #         raise ValueError('The given fingerprint sensor password is wrong!')
        #
        # except Exception as e:
        #     print('The fingerprint sensor could not be initialized!')
        #     print('Exception message: ' + str(e))
        #     exit(1)

        ## Gets some sensor information
        #print('Currently used templates: ' + str(f.getTemplateCount()) + '/' + str(f.getStorageCapacity()))
        ## Tries to search the finger and calculate hash
        try:
            # print('Waiting for finger...')
            ## Wait that finger is read
            while (f.readImage() == False):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            f.convertImage(0x01)
            ## Searchs template
            result = f.searchTemplate()
            positionNumber = result[0]

            if (positionNumber == -1):
                self.showFinger()
                # print("im here")
                # return None
                #print('No match found!\n Try Again!')

            else:
                ##print('The accuracy score is: ' + str(accuracyScore))
                pass

            if checkAlreadyVoted(str(positionNumber))==True:#FIREBASE CHECK IF ALREADY VOTED
                print("already voted")
                return None
            else:
                pass

            ## Loads the found template to charbuffer 1
            f.loadTemplate(positionNumber, 0x01)

            curs.execute("SELECT name,position FROM voters")
            nameList = []
            posList = []
            for name, position in curs.fetchall():
                nameList.append(name)
                posList.append(position)
            for i in range(len(posList)):
                if str(positionNumber) in posList[i]:
                    nameShow = nameList[i]
                    posShow = posList[i]
                    # self.off = Recognition()
                    # self.off.captureOff()
                    capcheck.append("yes")
                    self.openSecondWindow(nameShow,posShow)
                    print('Found Match')
                    widget.setCurrentIndex(widget.currentIndex() + 2)



        except Exception as e:

            print('Operation failed!')
            print('Exception message: ' + str(e))

    def openSecondWindow(self,name,pos):
        self.window7 = selectedResult()
        self.window7.namePOS(name,pos)
        print(name+pos)
        #widget.setCurrentIndex(widget.currentIndex()+1)

    def showFinger(self):
        msg = QMessageBox()
        msg.setWindowTitle("EVM Finger Message")
        msg.setText("The Finger is unregistered/didn't find a match\n"
                    "Click Retry to Try Again\n"
                    "Click Ok to do Face Authentication")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.buttonClicked.connect(self.popup_but)
        x = msg.exec_()

    def popup_but(self, i):
        itext = i.text()
        print(itext)
        if itext == "Retry":
            return None
        elif itext == "OK":
            widget.setCurrentIndex(widget.currentIndex() + 1)

###########################################################################################################################################


capcheck = []
nameget = []
class Recognition(QMainWindow):

    def __init__(self):
        super(Recognition, self).__init__()
        loadUi("faceRECOGNITIONWINDOW.ui", self)
        #self.exit.clicked.connect(self.exitrec)
        self.proceed.setEnabled(False)
        self.encoded()
        self.proceed.clicked.connect(self.proceedVote)
        self.webcam.clicked.connect(self.faceREC)

    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    @pyqtSlot()
    def encoded(self):
        faceencodePKL = open('faceencode.pkl', 'rb')
        faceencodeloop = pickle.load(faceencodePKL)
        for label, face_encoding in faceencodeloop:
            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(label)

    def faceREC(self):
        video_capture = cv2.VideoCapture(0)
        self.face_names = []
        if not video_capture.isOpened():
            sys.exit('Video source not found...')
        while True:
            ret, frame = video_capture.read()
            #if self.process_current_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            for face_encoding in self.face_encodings:
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)

                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if len(self.face_names) == 0:
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                    else:
                        name = "Unknown"
                    self.face_names.append(f'{name})')
                elif len(self.face_names) == 1:
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                    else:
                        name = "Unknown"
                    self.face_names.append(f'{name})')
                    if self.face_names[0] == self.face_names[1]:
                        self.namePrev.setText(name)
                        self.face_names.pop()
                        video_capture.release()
                        cv2.destroyAllWindows()
                        if checkAlreadyVotedName(name) == True:  # FIREBASE CHECK IF ALREADY VOTED
                            self.image.clear()
                            path = os.path.join(image_dir, name)
                            picture = os.path.join(path, "1.png")
                            self.image.setPixmap(QPixmap(picture))
                            return self.proceed.setEnabled(False),self.exit.setEnabled(True),self.camStatus.setText("already voted")
                        path = os.path.join(image_dir, name)
                        picture = os.path.join(path, "1.png")
                        self.image.setPixmap(QPixmap(picture))
                        return self.camStatus.setText("Found Match"), self.exit.setEnabled(False), self.proceed.setEnabled(True)
                    else:
                        self.image.clear()
                        self.face_names.clear()

            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)
            cv2.imshow('Face Recognition', frame)

            if cv2.waitKey(1) == ord('q'):
                break

    def proceedVote(self):
        count = call()
        if count == 2:
            curs.execute("SELECT name,position FROM voters")
            nameList = []
            posList = []

            for name, position in curs.fetchall():
                nameList.append(name)
                posList.append(position)
            for i in range(len(nameList)):
                if self.namePrev.text() == nameList[i]:
                    nameShow = nameList[i]
                    posShow = posList[i]
                    print(nameShow)
                    print(posShow)
                    print('Found Match')
                    self.nextwindow(nameShow, posShow)

    def nextwindow(self, name, pos):
        self.window7 = selectedResult()
        self.window7.namePOS(name, pos)
        widget.setCurrentIndex(widget.currentIndex() + 1)

#####################################################################################################################################
getResult = []
namE = []
poS = []




class instructionVoting(QMainWindow):
    def __init__(self):
        super(instructionVoting, self).__init__()
        loadUi('votersGui2.ui', self)
        self.nextButton.clicked.connect(self.presvote)

    def presvote(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

class presVote(QMainWindow):

    def __init__(self):
        super(presVote, self).__init__()
        loadUi('votersPres.ui', self)
        self.pres1.setCheckable(True)
        self.pres2.setCheckable(True)
        self.pres3.setCheckable(True)
        self.pres4.setCheckable(True)
        self.pres1.clicked.connect(self.togglepres1)
        self.pres2.clicked.connect(self.togglepres2)
        self.pres3.clicked.connect(self.togglepres3)
        self.pres4.clicked.connect(self.togglepres4)
        self.nextPres.clicked.connect(self.nextButPres)
        self.reset.clicked.connect(self.presuntoggle)

    def presuntoggle(self):
        for statusBut in [self.pres1,self.pres2,self.pres3,self.pres4]:
            if statusBut.isChecked() == True:
                statusBut.toggle()

    def togglepres1(self):
        if self.pres1.isChecked():
            for statusBut in [self.pres2,self.pres3,self.pres4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def togglepres2(self):
        if self.pres2.isChecked():
            for statusBut in [self.pres1, self.pres3, self.pres4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def togglepres3(self):
        if self.pres3.isChecked():
            for statusBut in [self.pres1, self.pres2, self.pres4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def togglepres4(self):
        if self.pres4.isChecked():
            for statusBut in [self.pres1, self.pres2, self.pres3]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def nextButPres(self):
        for statusBut in [self.pres1, self.pres2, self.pres3, self.pres4]:
            if statusBut.isChecked() == True:
                #print(statusBut.text())
                self.showVote(statusBut.text())
                widget.setCurrentIndex(widget.currentIndex() + 1)

    def showVote(self, getVote):
        window7 = selectedResult()
        window7.selected(getVote)

class viceVote(QMainWindow):

    def __init__(self):
        super(viceVote, self).__init__()
        loadUi('votersVice.ui', self)
        self.vice1.setCheckable(True)
        self.vice2.setCheckable(True)
        self.vice3.setCheckable(True)
        self.vice4.setCheckable(True)
        self.vice1.clicked.connect(self.togglevice1)
        self.vice2.clicked.connect(self.togglevice2)
        self.vice3.clicked.connect(self.togglevice3)
        self.vice4.clicked.connect(self.togglevice4)
        self.backVice.clicked.connect(self.backButVice)
        self.nextVice.clicked.connect(self.nextButVice)

    def untogglevice(self):
        for statusBut in [self.vice1, self.vice2, self.vice3, self.vice4]:
            if statusBut.isChecked() == True:
                statusBut.toggle()
                print("presdone")


    def togglevice1(self):
        if self.vice1.isChecked():
            for statusBut in [self.vice2,self.vice3,self.vice4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def togglevice2(self):
        if self.vice2.isChecked():
            for statusBut in [self.vice1, self.vice3, self.vice4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def togglevice3(self):
        if self.vice3.isChecked():
            for statusBut in [self.vice1, self.vice2, self.vice4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def togglevice4(self):
        if self.vice4.isChecked():
            for statusBut in [self.vice1, self.vice2, self.vice3]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def nextButVice(self):
        for statusBut in [self.vice1, self.vice2, self.vice3, self.vice4]:
            if statusBut.isChecked() == True:
                self.showVote(statusBut.text())
                widget.setCurrentIndex(widget.currentIndex() + 1)

    def showVote(self, getVote):
        window7 = selectedResult()
        window7.selected(getVote)

    def backButVice(self):
        getResult.pop()
        widget.setCurrentIndex(widget.currentIndex() - 1)

class secVote(QMainWindow):

    def __init__(self):
        super(secVote, self).__init__()
        loadUi('votersSec.ui', self)
        self.sec1.setCheckable(True)
        self.sec2.setCheckable(True)
        self.sec3.setCheckable(True)
        self.sec4.setCheckable(True)
        self.sec1.clicked.connect(self.togglesec1)
        self.sec2.clicked.connect(self.togglesec2)
        self.sec3.clicked.connect(self.togglesec3)
        self.sec4.clicked.connect(self.togglesec4)
        self.backSec.clicked.connect(self.backButSec)
        self.nextSec.clicked.connect(self.nextButSec)

    def untogglesec(self):
        for statusBut in [self.sec1, self.sec2, self.sec3, self.sec4]:
            if statusBut.isChecked() == True:
                statusBut.toggle()


    def togglesec1(self):
        if self.sec1.isChecked():
            for statusBut in [self.sec2,self.sec3,self.sec4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def togglesec2(self):
        if self.sec2.isChecked():
            for statusBut in [self.sec1, self.sec3, self.sec4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def togglesec3(self):
        if self.sec3.isChecked():
            for statusBut in [self.sec1, self.sec2, self.sec4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def togglesec4(self):
        if self.sec4.isChecked():
            for statusBut in [self.sec1, self.sec2, self.sec3]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def nextButSec(self):
        for statusBut in [self.sec1, self.sec2, self.sec3, self.sec4]:
            if statusBut.isChecked() == True:
                #print(statusBut.text())
                self.showVote(statusBut.text())
                widget.setCurrentIndex(widget.currentIndex() + 1)

    def showVote(self, getVote):
        window7 = selectedResult()
        window7.selected(getVote)

    def backButSec(self):
        getResult.pop()
        widget.setCurrentIndex(widget.currentIndex() - 1)

class treaVote(QMainWindow):

    def __init__(self):
        super(treaVote, self).__init__()
        loadUi('votersTrea.ui', self)
        self.trea1.setCheckable(True)
        self.trea2.setCheckable(True)
        self.trea3.setCheckable(True)
        self.trea4.setCheckable(True)
        self.trea1.clicked.connect(self.toggletrea1)
        self.trea2.clicked.connect(self.toggletrea2)
        self.trea3.clicked.connect(self.toggletrea3)
        self.trea4.clicked.connect(self.toggletrea4)
        self.backTrea.clicked.connect(self.backButTrea)
        self.nextTrea.clicked.connect(self.nextButTrea)


    def untoggletrea(self):
        for statusBut in [self.trea1, self.trea2, self.trea3, self.trea4]:
            if statusBut.isChecked() == True:
                statusBut.toggle()

    def toggletrea1(self):
        if self.trea1.isChecked():
            for statusBut in [self.trea2,self.trea3,self.trea4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def toggletrea2(self):
        if self.trea2.isChecked():
            for statusBut in [self.trea1, self.trea3, self.trea4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def toggletrea3(self):
        if self.trea3.isChecked():
            for statusBut in [self.trea1, self.trea2, self.trea4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def toggletrea4(self):
        if self.trea4.isChecked():
            for statusBut in [self.trea1, self.trea2, self.trea3]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def nextButTrea(self):
        for statusBut in [self.trea1, self.trea2, self.trea3, self.trea4]:
            if statusBut.isChecked() == True:
                #print(statusBut.text())
                self.showVote(statusBut.text())
                window7.result()
                widget.setCurrentIndex(widget.currentIndex() + 1)

    def showVote(self,getVote):
        window7 = selectedResult()
        window7.selected(getVote)

    def backButTrea(self):
        getResult.pop()
        widget.setCurrentIndex(widget.currentIndex() - 1)

class selectedResult(QMainWindow):

    def __init__(self):
        super(selectedResult, self).__init__()
        loadUi('votersPreview.ui', self)
        self.backSelect.clicked.connect(self.backButSelect)
        self.finalizeSelect.clicked.connect(self.finalizeVote)


    def selected(self,candidates):
        getResult.append(candidates)

    def result(self):
        self.presSelect.setText(getResult[0])
        self.viceSelect.setText(getResult[1])
        self.secSelect.setText(getResult[2])
        self.treaSelect.setText(getResult[3])

    def backButSelect(self):
        getResult.pop()
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def namePOS(self, name, pos):
        namE.append(name)
        poS.append(pos)
        print(namE)
        print(poS)

    def finalizeVote(self):
        for pos in poS:
            poss = pos
        for name in namE:
            namee = name
        finalizeFire(namee, poss ,getResult[0],getResult[1],getResult[2],getResult[3])
        #printcandidates(getResult[0],getResult[1],getResult[2],getResult[3])
        self.pres = presVote()
        self.pres.presuntoggle()
        print("done")
        self.vice = viceVote()
        self.vice.untogglevice()
        self.sec = secVote()
        self.sec.untogglesec()
        self.trea = treaVote()
        self.trea.untoggletrea()
        poS.clear()
        getResult.clear()
        namE.clear()
        capcheck.clear()
        nameget.clear()
        widget.setCurrentIndex(widget.currentIndex() + 1)

class thankyou(QMainWindow):

    def __init__(self):
        super(thankyou, self).__init__()
        loadUi('thankyou.ui', self)
        self.done.clicked.connect(self.done1)

    def done1(self):
        widget.setCurrentIndex(0)

app=QApplication(sys.argv)
window = Voting()
windowRec = Recognition()
window2 = instructionVoting()
window3 = presVote()
window4 = viceVote()
window5 = secVote()
window6 = treaVote()
window7 = selectedResult()
window8 = thankyou()

widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.addWidget(windowRec)
widget.addWidget(window2)
widget.addWidget(window3)
widget.addWidget(window4)
widget.addWidget(window5)
widget.addWidget(window6)
widget.addWidget(window7)
widget.addWidget(window8)
window.setFixedWidth(800)
window.setFixedHeight(600)
# windowRec.setFixedWidth(800)
# windowRec.setFixedHeight(600)
#widget.showFullScreen()
widget.show()

try:
    sys.exit(app.exec_())
    conn.close()
except:
    print('exiting')
    conn.close()
