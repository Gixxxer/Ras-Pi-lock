
#Edited By Chris Rigby


import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import Lights
GPIO.setwarnings(False)
reader = SimpleMFRC522.SimpleMFRC522()

def loclite():
	Lights.bluelight()
	time.sleep(2)


def writetocard():	
	
	try:
			print("Place card on reader please.")
			id=reader.read()
			print("Type first name and last name (lowercase only) separated by a comma and press enter.")
			text = raw_input('New data:')
			print("Now place your tag to write.")
			reader.write(text)
			id=reader.read()
			print("Written")
			print(id)
			print(text)
			print("Press enter to exit.")
			line=(str(id)+ "," + str(text) + "\n")
			newline1=line.replace("'","")
			newline2=newline1.strip("(")
			with open("Users.txt","a+") as f:
				f.write(newline2)
      
	finally:
		GPIO.cleanup()



