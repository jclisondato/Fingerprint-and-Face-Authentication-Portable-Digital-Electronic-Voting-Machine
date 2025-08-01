import RPi.GPIO as GPIO
import time

power_relay = 12
rpi_relay = 13

# turn off the cameras to save the recording
GPIO.output(power_relay, GPIO.HIGH)
GPIO.output(rpi_relay, GPIO.HIGH)
time.sleep(3)
# start recording
GPIO.output(power_relay, GPIO.LOW)
GPIO.output(rpi_relay, GPIO.HIGH)

