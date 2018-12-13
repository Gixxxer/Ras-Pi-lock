# Written by Chris Rigby
import RPi.GPIO as GPIO
import time
# "GPIO19 = Green "
# "GPIO16 = Red "
# "GPIO26 = Blue "

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

cleanup = GPIO.cleanup



# Green on 1 sec then off
def greenlight():
    GPIO.setup(19,GPIO.OUT)
    print("LED on")
    GPIO.output(19,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(19,GPIO.LOW)
    cleanup



# Red on 1 sec then off 
def redlight():    
    GPIO.setup(16,GPIO.OUT)
    print("LED on")
    GPIO.output(16,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(16,GPIO.LOW)
    cleanup

# Blue on 1 sec then off
def bluelight():
    GPIO.setup(26,GPIO.OUT)
    print("LED on")
    GPIO.output(26,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(26,GPIO.LOW)
    cleanup


