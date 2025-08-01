"""
Test the Arduino and RPI communication. 
This script is used to make sure that the camera is being released and aquisitioned at the right time
Author: Emnma Smith
Date Modified: 18 April 2019
"""

import os 
import RPi.GPIO as GPIO
import time
import threading


CAM_REQUEST = 5 # this will be high if we recieve a request for the cameras
CAM_READY = 3 # we will set this high after we have unmounted the cameras


GPIO.setmode(GPIO.BOARD)
# Set the pin used to indicate that the camera has been requested to an input with a PD resistor
# LOW = no request, HIGH = request
GPIO.setup(CAM_REQUEST, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# Indicate that the camers are mounted to the RPI at startup
GPIO.setup(CAM_READY, GPIO.OUT, initial=GPIO.LOW)


def release_cameras():
    os.system('sudo umount -l /media/pi/5C9F-199C')
    GPIO.output(CAM_READY, GPIO.HIGH)
    print("Cameras are gone now")


# After the cameras are released by the Arduino, they should automatically remount 
# to the pi and thus will not be ready anymore
def cameras_mounted():
    GPIO.output(CAM_READY, GPIO.LOW)
    print("Cameras would be back now")

def camera_handler(pin):
    status = GPIO.input(pin)
    if pin == CAM_REQUEST and status: # if the camera was requested
        release_cameras()
    elif pin == CAM_REQUEST and not status: # if the arduino is done recording
        cameras_mounted()
    else:
        print("Camera handler fired without a CAM_REQUEST change\nThis should be impossible")


GPIO.add_event_detect(CAM_REQUEST, GPIO.BOTH, camera_handler)

# Busy loop. Can be filled with something useful
while True:
    time.sleep(0.001)
