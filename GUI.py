#!/usr/bin/env python
# Written By Chris Rigby
# Program is designed to only have one admin credential currently
# many keycards can be an Admin
from Tkinter import *  # import base classes
import Tkinter as tk
import tkMessageBox  # import message box classes
import Relay # controlls relay activation
import RPi.GPIO as GPIO  # GPIO settings
import time # imports time functions
import os # lets me enter commands to console
import Write # write functions for card
import SimpleMFRC522
GPIO.setmode(GPIO.BCM)  # sets GPIO Pins to GPIO numbers instead of board pin numbers
GPIO.setwarnings(False)  # turns off annoying warnings
cleanup = GPIO.cleanup  # cleans up import scripts for startup






#Lights 
#Finished
# "GPIO19 = Green "
# "GPIO16 = Red "
# "GPIO26 = Blue "
# Green on 1 sec then off
def greenlight():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19,GPIO.OUT)
    print("LED on")
    GPIO.output(19,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(19,GPIO.LOW)
    cleanup



# Red on 1 sec then off
def redlight():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT)
    print("LED on")
    GPIO.output(16,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(16,GPIO.LOW)
    cleanup

# Blue on 1 sec then off
def bluelight():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    print("LED on")
    GPIO.output(26, GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(26, GPIO.LOW)
    cleanup
    
    
    

# Message boxes
# Finished
def printadduser():  # Message box function
    greenlight()
    tkMessageBox.showinfo("Add User", "New User Added.")

def printdeleteuser():  # Message box function
    redlight()
    tkMessageBox.showinfo("Delete User", "User Deleted.")

def printlog():  # Message box function
    bluelight()
    tkMessageBox.showinfo("Log", "Current log copied to desktop.")

def printadmindelete():  # Message box function
    redlight()
    tkMessageBox.showinfo("Admin Delete", "All users deleted except for admin.")

def copylog(): # fixed copies log 

    os.system("cd /home/pi/Desktop")  # log directory
    os.system("cp PILog.txt pilogcopy.txt ")  #BASH copy log   *****Update directory
    os.system("mv pilogcopy.txt /home/pi")      # Bash Move copy *****Update directory

def logaction(): # combines log copy and lights for button push
		copylog()
		printlog()


def adduser(): # combines new user card writing and lights for button push
		GPIO.setmode(GPIO.BCM)
		Write.writetocard()
		printadduser()

def deleteall(): # query active users and delete all but admin
 f= open("Users.txt","r")
 lines=f.readlines()
 f.close
 f= open("Users.txt","w")
 for line in lines:
	 if "admin" in line:
		 f.write(line)
	 elif "admin" not in line:
			 f.write("")

def nukeall(): # combines delete all but admin and lights for button push
	deleteall()
	printadmindelete()



# Deleted some things from GUI, thats why numbers are off.

# GUI Code start

root = Tk()  # create blank window = root
root.geometry("250x300")
root.title("Admin Control")  # window title
root.resizable(0, 0)  # keeps window from changing sizes

#Finished
btnAddUser = Button(text="Add User", fg="Green", command=adduser)  # add users button
btnAddUser.grid(row=6, column=1)
btnAddUser.grid(sticky=EW)

#btnDeleteUser = Button(text="Delete User", fg="Red", command=printdeleteuser)  # deletes individual users users, phase 2
#btnDeleteUser.grid(row=7, column=1)
#btnDeleteUser.grid(sticky=EW)

#Finished, overites existing copy
btnExportLog = Button(text="Export Log", fg="Black", command=logaction)  # brings log file to desktop
btnExportLog.grid(row=8, column=1)
btnExportLog.grid(sticky=EW)


#Finished
scrollbar = Scrollbar(root, orient=VERTICAL)  # scrollbar
scrollbar.grid(row=9, column=2, sticky=N+S+E)  # scrollbar placement

#Finished
list1 = Listbox(root, yscrollcommand=scrollbar.set)  # listbox and scrollbar action command
list1.grid(row=9, column=1)
scrollbar.config(command=list1.yview)
#with open("Users.txt","r") as userlist: # puts current user list on display at program start
    #for line in userlist:
		#part=line.split(",")
		#newname=(part[1]+" "+part[2])
		#list1.insert(1, (newname.strip("'\n")))

def userslist():
	with open("Users.txt","r") as userlist: # puts current user list on display for button
		for line in userlist:
			part=line.split(",")
			newname=(part[1]+" "+part[2])
			list1.insert(1, (newname.strip("'\n")))
def clearlist():
	list1.delete(0,END) # clears listbox

def updateusers(): # clears listbox and repopulates with list action for button
	clearlist()
	userslist()
#Finished
btnListUser = Button(text="Current Users", fg="Black",command=updateusers)  # brings shows current users in listbox
btnListUser.grid(row=11, column=1)
btnListUser.grid(sticky=EW)

def delete():
	 f= open("Users.txt","r")
	 lines=f.readlines()
	 f.close
	 f= open("Users.txt","w")
	 for line in lines:
		 if "admin" in line:
			f.write(line)
		 elif "admin" not in line:
				f.write("")
			

#Finished - repath delete file
btnDeleteAll = Button(text="Delete All but Admin", fg="Red", command=nukeall)  # deletes all but admin
btnDeleteAll.grid(row=12, column=1)
btnDeleteAll.grid(sticky=EW)


root.mainloop()  # keeps GUI up until exited

# GUI code end                                                                                              GUI code End

