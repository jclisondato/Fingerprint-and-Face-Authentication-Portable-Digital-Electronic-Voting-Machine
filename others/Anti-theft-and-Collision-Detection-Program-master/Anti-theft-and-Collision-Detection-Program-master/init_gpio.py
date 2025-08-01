# This will be used to initialize
# all of the GPIO pins as needed 

import RPi.GPIO as GPIO
import time

power_relay = 12
rpi_relay =13 
arduino_to_pi = 7
pi_to_arduino =11 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(power_relay, GPIO.OUT)
GPIO.setup(rpi_relay, GPIO.OUT)
GPIO.setup(arduino_to_pi, GPIO.OUT)
GPIO.setup(pi_to_arduino, GPIO.OUT)

while(True):
    time.sleep(1)

GPIO.cleanup()



