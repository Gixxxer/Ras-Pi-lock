# Written By Chris Rigby

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# "GPIO27 = Relay "


GPIO.setwarnings(False)

cleanup = GPIO.cleanup()



# Relay on 3 sec then off
def openlock():
    cleanup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    print("Unlock")
    GPIO.output(27,GPIO.LOW)
    time.sleep(3)
    print("Locked")
    GPIO.output(27,GPIO.HIGH)
    cleanup




