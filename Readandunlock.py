#!/usr/bin/env python
# unknown creator
# part of the RFC522 package by Simon Monk https://github.com/simonmonk/
#Modified By Chris Rigby

import RPi.GPIO as GPIO  # GPIO
import SimpleMFRC522  # Classes for opperation
import datetime  # date adn time
import time  # timer
import Lights  # lights script
import Relay  # relay script
GPIO.setmode(GPIO.BCM)  # sets GPIO by number not pin
GPIO.setwarnings(False)  # gets rid of annoying warning
today = datetime.datetime.now()  # date/time now
logdate = str(today.strftime("%Y-%m-%d %H:%M"))  # modifies date time to format I wanted
reader = SimpleMFRC522.SimpleMFRC522()  # reader classes
print("Place card on reader please.")  # user direction
def loclite():  # combines lights and relay access 
	Lights.greenlight()  # lights
	time.sleep(2)  # time between scans
	Relay.openlock() # power to relay.
def rejectlite():  # combines lights and relay access 
	Lights.redlight()  # lights
	time.sleep(2)  # time between scans

def readinwrite(): # continuous loop for scan and entry into log file
    try:
        while True:
			GPIO.setmode(GPIO.BCM)
			id, text = reader.read()  # read in card info
 			print(id)  # card serial
			print(text)  # user Name
			print(logdate)  # todays date and time for log entry
			time.sleep(3)
			f= open("Users.txt","r")
			lines=f.readlines()
			for line in lines:
				if str(id) in line:
					print("yes")
					loclite()
					logfile = open("PILog.txt","a+")  # log appending
					logfile.write(str(id) + "," + logdate + "," + text + "\n" )  # format for log entry
					logfile.close # close log
				elif str(id) not in line:
						print(text)
						rejectlite()
						logfile = open("PILog.txt","a+")  # log appending
						logfile.write(str(id) + "," + logdate + "," + text + "\n" )  # format for log entry
						logfile.close # close log
			f.close		
			GPIO.cleanup()
			
    finally:
                
                GPIO.cleanup()
readinwrite()
