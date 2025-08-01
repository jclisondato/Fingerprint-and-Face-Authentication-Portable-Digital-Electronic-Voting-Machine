# Phong Nguyen
# ECE 412, Winter 2019
# Capstone Project: Anti-theft and Collision detection
# 4/3/2019

import sys
import datetime
from PyQt5.QtWidgets import QApplication
from mainmenu_f import mainmenuwindow
from passcode_f import passcodewindow
from change_passcode_f import change_passcodewindow
from root_f import rootwindow
from fac_rec_f import fac_recwindow
from security_f import securitywindow
from start_car_f import start_carwindow
from manage_drivers_f import manage_driverswindow
from name_new_user_f import name_new_userwindow
from cap_new_user_f import cap_new_userwindow
from trainer_f import trainerwindow
from adjust_fac_rec_f import adjust_fac_recwindow
from remove_a_driver_f import remove_a_driverwindow
from review_footage_f import review_footagewindow
from video_playback_f import video_playbackwindow
from error_f import errorwindow
from error_fac_rec_f import error_fac_recwindow
from PyQt5.QtCore import QTimer
import subprocess
import json
import glob
from PyQt5 import QtTest
import RPi.GPIO as GPIO

#320,240
import os.path
import os
import numpy as np
import numbers
from PIL import Image

time_now = datetime.datetime.now()


# configuration
config_json='conf/conf.json'
# data for training
dataset='dataset/'

#save.txt
save_path='save.txt'

#path to yml
yml_path=('trainer/trainer.yml')

# Full screen mode
full_screen =1 
# Use pi cam
usepicam=1

# timer for root menu 60 seconds
timer_for_root=120

# counter for timer
counter=0

#trainer flag for for restart
trainer_flag=0

#Camera Directory
LEFT_CAMERA='/media/pi/L_CAMERA/'
RIGHT_CAMERA='/media/pi/R_CAMERA/'
FRONT_CAMERA='/media/pi/F_CAMERA/'
BACK_CAMERA='/media/pi/B_CAMERA/'


#setup mode
GPIO.setmode(GPIO.BOARD)



GPIO_START_CAR = 40
GPIO_ARD=7
GPIO_COMMAND_ARD =11

# Set up inputs and outputs

GPIO.setup(GPIO_START_CAR, GPIO.OUT)

#OUT COME LINE ARUINO
GPIO.setup(GPIO_ARD, GPIO.IN)

#IN COME LINE ARUINO
GPIO.setup(GPIO_COMMAND_ARD, GPIO.OUT)


app = QApplication(sys.argv)
timer_back2main = QTimer()

timer_button_enable = QTimer()
timer_ack = QTimer()

# global
camera = ''
CAM_OFF_TIME = 3000

# Read conf json
def read_json():
    with open(config_json, 'r') as fp:
        return json.load(fp)

# Write conf json
def write_json(file,data):
     with open(file,'w') as fp:
         json.dump(data,fp)



def timer_process():
    global counter,timer_for_root
    counter=timer_for_root
    # 1 second each
    if not timer_back2main.isActive():
        timer_back2main.start(1000)


def time_handler():
        global counter
        counter -= 1

        if root.isVisible():
            # lcdNumber root
            root.lcdNumber.display(counter)
            # lcdNumber start car
        elif start_car.isVisible():
            start_car.lcdNumber.display(counter)

        #lcdNumber
        if counter <=0:
            timer_back2main.stop()
            back_to_main()




# from passcode_to_root
def open_root():
    GPIO.output(GPIO_START_CAR, GPIO.LOW)

    if fac_rec.isVisible():
        fac_rec.timer_main.stop()
        fac_rec.close()

    security.close()
    review_footage.close()
    adjust_fac_rec.close()
    change_passcode.close()
    passcode.close()
    start_car.close()
    manage_drivers.close()




    if trainer.isVisible():
        trainer.timer_back2root.stop()
        trainer.close()


    if passcode.timer2root.isActive():
        passcode.timer2root.stop()

    if change_passcode.timer2root.isActive():
        change_passcode.timer2root.stop()
    # count down 60 seconds to exitting
    timer_process()



#||||||||||||||||||||||||||||||||||
# Update camera state from json file
# camera state 1 is accessing
# camera state 0 is recording
    # load config json for speech
    my_config = read_json()

    # getting speech flag for fac_rec
    camera = int(my_config.get('camera', ''))
    if camera:
        camera = 'ACCESSING'
        enable_review_footage()
        #scanning for directory
        #subprocess.run(["sudo", "python", "resetusb.py", "Terminus"])
    else:
        camera = 'RECORDING'
        disable_review_footage()

    # showing speech status
    root.camera_button.setText('Cameras:\n' + camera)

#||||||||||||||||||||||||||||||||||

    # start root
    root.start()
    if full_screen:
        root.showFullScreen()
    else:
        root.show()



#from passcode or root to main
def back_to_main():
    # global trainer_flag
    # if trainer_flag:
    #     os.execl(sys.executable, sys.executable, *sys.argv)
    # else:
        #close possible open window
    GPIO.output(GPIO_START_CAR, GPIO.LOW)

    GPIO.cleanup()

    if fac_rec.timer.isActive():
        fac_rec.cap.stop()
        fac_rec.timer.stop()

        QtTest.QTest.qWait(1500)

        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        passcode.close()
        fac_rec.close()
        root.close()
        error_fac_rec.close()

        #check timers and stop them
        if timer_back2main.isActive():
            timer_back2main.stop()

        if passcode.timer2main.isActive():
            passcode.timer2main.stop()


        os.execl(sys.executable, sys.executable, *sys.argv)

        # if full_screen:
        #     mainmenu.showFullScreen()
        # else:
        #     mainmenu.show()


#from main to passcode
def open_passcode():
    mainmenu.close()
    passcode.lineEdit.clear()
    if full_screen:
        passcode.showFullScreen()
    else:
        passcode.show()

def open_change_passcode():
    security.close()
    change_passcode.lineEdit.clear()

    if full_screen:
        change_passcode.showFullScreen()
    else:
        change_passcode.show()

def open_adjust_fac_rec():
    security.close()
    if full_screen:
       adjust_fac_rec.showFullScreen()
    else:
       adjust_fac_rec.show()
       adjust_fac_rec.start()

def open_security():
    adjust_fac_rec.close()
    change_passcode.close()
    root.close()
    #check timers and stop them
    if timer_back2main.isActive():
        timer_back2main.stop()

    if full_screen:
        security.showFullScreen()
    else:
        security.show()




#from main to facial recognition
def open_fac_rec():
    global usepicam
    mainmenu.close()


    if os.path.isfile(yml_path):
        # load config json for speech
        my_config = read_json()

        # getting speech flag for fac_rec
        fac_rec.speech = int(my_config.get('speech', ''))

        # start fac_rec camera
        fac_rec.camera_init()

        if full_screen:
            fac_rec.showFullScreen()
        else:
            fac_rec.show()
    else:
        #open error_fac_rec
        open_error_fac_rec()


#==========================================================================================================================
#===================IMPORTANT TURN ON THE CAR RIGHT HERE==================================================================
def open_start_car():
   # root.start_car_button.setEnabled(False)

    fac_rec.close()
    passcode.close()
    root.close()
    #count down 60 seconds to exitting
    timer_process()

    GPIO.output(GPIO_START_CAR, GPIO.HIGH)

    if fac_rec.timer.isActive():
        fac_rec.timer.stop()
        fac_rec.cap.release()
    if full_screen:
        start_car.showFullScreen()
    else:
        start_car.show()
#==========================================================================================================================
#==========================================================================================================================
#---------------------------------------------------------------------------------------------------

def open_manage_drivers():
    root.close()
    name_new_user.close()
    cap_new_user.close()
    remove_a_driver.close()
    #check timers and stop them
    if timer_back2main.isActive():
        timer_back2main.stop()

    if cap_new_user.timer3.isActive():
        # stop timer
        cap_new_user.timer3.stop()


    if full_screen:
        manage_drivers.showFullScreen()
    else:
        manage_drivers.show()

def open_name_new_user():
    manage_drivers.close()
    error.close()
    name_new_user.lineEdit.clear()
    if full_screen:
        name_new_user.showFullScreen()
    else:
        name_new_user.show()

def open_cap_new_user(Id,new_name):
    name_new_user.close()
    cap_new_user.Id=Id
    cap_new_user.new_name=new_name

    # load config json for speech
    my_config = read_json()

    # getting speech flag for fac_rec
    cap_new_user.speech = int(my_config.get('speech', ''))

    cap_new_user.camera_init()
    if full_screen:
        cap_new_user.showFullScreen()
    else:
        cap_new_user.show()

def open_remove_a_driver():
    manage_drivers.close()
    remove_a_driver.remove_f()
    if full_screen:
        remove_a_driver.showFullScreen()
    else:
        remove_a_driver.show()

def remove_all():
    if os.path.isfile(save_path):
        os.remove(save_path)
    if os.path.isfile(yml_path):
        os.remove(yml_path)

    files = glob.glob('dataset/*')
    for f in files:
        os.remove(f)
    files = glob.glob('preview/*')
    for f in files:
        os.remove(f)



#open check error before process
def check_error():
    driver_name = name_new_user.lineEdit.text()

    name_array = []
    # open save.txt
    if os.path.isfile(save_path):
        with open(save_path, 'r+') as my_file:
            name_array = my_file.readlines()

        # GUI prompt user to enter their name
    new_name = driver_name


    # GUI new_name valid or invalid
    if (new_name + '\n') in name_array or new_name == '':
        open_error()
    else:
        # write new name to file
        my_file = open(save_path, 'a+')
        my_file.write(new_name + '\n')
        my_file.close()

        # add new name to the end of the list
        name_array.append(new_name)

        # id base on position in name array. 0 dont count
        Id = len(name_array)


        open_cap_new_user(Id,new_name)


def open_trainer():
    global trainer_flag
    trainer_flag=1
    # list names in dataset directory
    name_array = os.listdir(dataset)
    manage_drivers.close()
    if name_array:
        if full_screen:
            trainer.showFullScreen()
        else:
            trainer.show()
        trainer.start()
    else:
        open_root()

def open_review_footage():
    root.close()

    # check timers and stop them
    if timer_back2main.isActive():
        timer_back2main.stop()

    # camera Directory
    left_camera = ''
    right_camera = ''
    front_camera = ''
    back_camera = ''

    update_time = str(time_now.year) + str(time_now.month).zfill(2) + str(time_now.day).zfill(2) + str(
        time_now.hour).zfill(2) + str(time_now.hour).zfill(2) + str(time_now.minute).zfill(2) + str(
        time_now.second).zfill(2)+' '+'Y'
    if os.path.isdir(LEFT_CAMERA):
        left_camera = LEFT_CAMERA+'VIDEO'
        file_l = open(LEFT_CAMERA+'TIMEREST.txt', 'w')
        file_l.write(update_time)
        file_l.close()

    if os.path.isdir(RIGHT_CAMERA):
        right_camera = RIGHT_CAMERA+'VIDEO'
        file_r = open(RIGHT_CAMERA+'TIMEREST.txt', 'w')
        file_r.write(update_time)
        file_r.close()

    if os.path.isdir(FRONT_CAMERA):
        front_camera = FRONT_CAMERA+'VIDEO'
        file_f = open(FRONT_CAMERA+'TIMEREST.txt', 'w')
        file_f.write(update_time)
        file_f.close()

    if os.path.isdir(BACK_CAMERA):
        back_camera = BACK_CAMERA+'VIDEO'
        file_b = open(BACK_CAMERA+'TIMEREST.txt', 'w')
        file_b.write(update_time)
        file_b.close()




    review_footage.list_left.setRootIndex(review_footage.fileModel.setRootPath(left_camera))
    review_footage.list_right.setRootIndex(review_footage.fileModel.setRootPath(right_camera))
    review_footage.list_front.setRootIndex(review_footage.fileModel.setRootPath(front_camera))
    review_footage.list_back.setRootIndex(review_footage.fileModel.setRootPath(back_camera))
    if full_screen:
        review_footage.showFullScreen()
    else:
        review_footage.show()




def back_to_review_footage():
    video_playback.player.stop()
    video_playback.close()


def open_video_playback():
    review_footage.timer_video_playback.stop()

    #review_footage.path

    if full_screen:
        video_playback.showFullScreen()
    else:
        video_playback.show()

    video_playback.start(review_footage.path)



def open_error():
    name_new_user.close()
    if full_screen:
        error.showFullScreen()
    else:
        error.show()


def open_error_fac_rec():
    mainmenu.close()
    if full_screen:
        error_fac_rec.showFullScreen()
    else:
        error_fac_rec.show()








def enable_review_footage():
    # enable camera button
    root.review_footage_button.setEnabled(True)
    root.review_footage_button.setStyleSheet("color: white; border: 3px solid red;")

def disable_review_footage():
    # disable review footage button
    root.review_footage_button.setEnabled(False)
    root.review_footage_button.setStyleSheet("color: Gray; border: 3px solid gray;")

def enable_camera_button():
    global camera
    timer_button_enable.isActive()
    timer_button_enable.stop()

    # enable camera button
    root.camera_button.setEnabled(True)
    root.camera_button.setStyleSheet("color: white; border: 3px solid red;")
    if camera == 'RECORDING':
        disable_review_footage()
    else:
        enable_review_footage()

def disable_camera_button():
    global camera
    if camera == 'RECORDING':
        disable_review_footage()
    # disable camera button
    root.camera_button.setEnabled(False)
    #root.camera_button.setStyleSheet("color: Gray; border: 3px solid gray;")
    timer_button_enable.start(5000)


def change_camera2recording():
    global camera
    camera = 'RECORDING'
    my_config = read_json()
    my_config['camera'] = '0'
    write_json(config_json, my_config)
    root.camera_button.setText('Cameras:\n' + camera)

    if os.path.exists('/media/pi/L_CAMERA'):
        subprocess.run(["sudo", "umount", "-l", "/media/pi/L_CAMERA"])
    if os.path.exists('/media/pi/F_CAMERA'):
        subprocess.run(["sudo", "umount", "-l", "/media/pi/F_CAMERA"])
    if os.path.exists('/media/pi/B_CAMERA'):
        subprocess.run(["sudo", "umount", "-l", "/media/pi/B_CAMERA"])
    if os.path.exists('/media/pi/R_CAMERA'):
        subprocess.run(["sudo", "umount", "-l", "/media/pi/R_CAMERA"])

    GPIO.output(GPIO_COMMAND_ARD, GPIO.LOW)

    # disable camera button 5 seconds
    disable_camera_button()




def change_camera2accessing():
    global camera
    GPIO.output(GPIO_COMMAND_ARD, GPIO.HIGH)
    camera = 'ACCESSING'
    my_config = read_json()
    my_config['camera'] = '1'
    # showing camera status
    write_json(config_json, my_config)
    root.camera_button.setText('Cameras:\n' + camera)


    # disable camera button 4 seconds
    disable_camera_button()

    # scanning for directory
    #subprocess.run(["sudo", "python", "resetusb.py", "Terminus"])

def IRQ_camera2accessing():
    global camera
    GPIO.output(GPIO_COMMAND_ARD, GPIO.HIGH)
    camera = 'ACCESSING'
    my_config = read_json()
    my_config['camera'] = '1'
    # showing camera status
    write_json(config_json, my_config)
    root.camera_button.setText('Cameras:\n' + camera)

    # scanning for directory
    #subprocess.run(["sudo", "python", "resetusb.py", "Terminus"])
    enable_review_footage()

    # disable camera button 4 seconds
    #disable_camera_button()

# change camera state
def change_camera():
    global camera
    # load config json for speech
    my_config = read_json()

    # getting speech flag for fac_rec
    camera = int(my_config.get('camera', ''))


    # accessing->recording
    if camera:
        change_camera2recording()

    # recording -> accessing
    else:
        change_camera2accessing()


def IRQ_collision(channel):
    # print("Got to interrupt\n")
    # # load config json for speech
    # my_config = read_json()
    # print("Should have read json\n")
    # GPIO.output(GPIO_RASP_ACK,GPIO.LOW)
    # # getting speech flag for fac_rec
    # camera = int(my_config.get('camera', ''))
    # if camera:
    #     pass
    # else:
    #     change_camera2accessing()
    # GPIO.output(GPIO_RASP_ACK, GPIO.HIGH)
    # timer_ack.start(1000)
    if GPIO.input(channel):
        IRQ_camera2accessing()




#Load the camera setting
#subprocess.run(["uvcdynctrl","-L","cam.gpf1"])


#object instantiation
mainmenu = mainmenuwindow()
passcode = passcodewindow()
change_passcode = change_passcodewindow()
root = rootwindow()
start_car = start_carwindow()
manage_drivers = manage_driverswindow()
name_new_user = name_new_userwindow()
cap_new_user = cap_new_userwindow()
fac_rec = fac_recwindow()
trainer=trainerwindow()
security=securitywindow()
adjust_fac_rec = adjust_fac_recwindow()
remove_a_driver = remove_a_driverwindow()
review_footage = review_footagewindow()
video_playback = video_playbackwindow()
error = errorwindow()
error_fac_rec = error_fac_recwindow()


GPIO.output(GPIO_START_CAR, GPIO.LOW)
#start with mainmenu

# load config json for speech
my_config = read_json()


if full_screen:
    mainmenu.showFullScreen()
else:
    mainmenu.show()

#timer camera button
timer_button_enable.timeout.connect(enable_camera_button)
#timer back2main
timer_back2main.timeout.connect(time_handler)
passcode.timer2main.timeout.connect(back_to_main)
# timer to root
passcode.timer2root.timeout.connect(open_root)
change_passcode.timer2root.timeout.connect(open_root)
trainer.timer_back2root.timeout.connect(open_root)

#timer_to_manage_drivers
cap_new_user.timer3.timeout.connect(open_manage_drivers)



#button tree
mainmenu.passcode_button.clicked.connect(open_passcode)
mainmenu.facial_button.clicked.connect(open_fac_rec)


passcode.backtomainmenu_button.clicked.connect(back_to_main)
change_passcode.backtomainmenu_button.clicked.connect(open_security)

root.backtomainmenu_button2.clicked.connect(back_to_main)
root.start_car_button.clicked.connect(open_start_car)
root.manage_drivers_button.clicked.connect(open_manage_drivers)
root.review_footage_button.clicked.connect(open_review_footage)
root.security_button.clicked.connect(open_security)
root.camera_button.clicked.connect(change_camera)


security.adjust_threshold.clicked.connect(open_adjust_fac_rec)
security.change_passcode.clicked.connect(open_change_passcode)
security.back_to_root.clicked.connect(open_root)

fac_rec.backtomainmenu_button3.clicked.connect(back_to_main)
fac_rec.timer_main.timeout.connect(open_root)

start_car.back_to_root.clicked.connect(open_root)

adjust_fac_rec.back.clicked.connect(open_security)

review_footage.back_to_root.clicked.connect(open_root)
review_footage.timer_video_playback.timeout.connect(open_video_playback)

video_playback.back_button.clicked.connect(back_to_review_footage)


manage_drivers.add_driver.clicked.connect(open_name_new_user)
manage_drivers.remove_driver.clicked.connect(open_remove_a_driver)
manage_drivers.remove_all.clicked.connect(remove_all)
manage_drivers.backtoroot.clicked.connect(open_trainer)

name_new_user.backtomanagedrivers_button.clicked.connect(open_manage_drivers)
name_new_user.benter.clicked.connect(check_error)

remove_a_driver.back.clicked.connect(open_manage_drivers)

error.back.clicked.connect(open_name_new_user)
error_fac_rec.pushButton.clicked.connect(back_to_main)




# GPIO interrupt
GPIO.add_event_detect(GPIO_ARD, GPIO.RISING, callback=IRQ_collision)


sys.exit(app.exec_())

