# This will put the cameras in accessing mode

import RPi.GPIO as GPIO
import time

power_relay = 12
rpi_relay = 13

# turn off the cameras to save the recording
GPIO.output(power_relay, GPIO.HIGH)
GPIO.output(rpi_relay, GPIO.HIGH)
time.sleep(3)
# connect the camera to the Rpi
GPIO.output(power_relay, GPIO.LOW)
GPIO.output(rpi_relay, GPIO.LOW)

