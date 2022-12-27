#!/usr/bin/env python3

"""
alarm.py
Ashley Ung 

This program functions as an alarm. It will ask the user for an alarm time and then set the alarm to play the alarm sound when the current time matches the alarm time.  
"""

from playsound import playsound
import time
import threading
import pygame

# Function to play the alarm sound. Loads the alarm sound, this file named "alarm.mp3", is downloaded from an external source
def playAlarm (alarmTime):
	pygame.mixer.init()
	pygame.mixer.music.load ("alarm.mp3")
	while True:
		currentTime = time.strftime ("%H:%M")
		if currentTime == alarmTime:
			print ("Wake up and have a great day!")
			playsound ("alarm.mp3")
			break
		
# Obtain the alarm time from the user
alarmTime = input ("Enter the time for the alarm (HH:MM): ") # Uses military time notation

# Create a thread to run the alarm in the background
alarmThread = threading.Thread (target = playAlarm, args = (alarmTime,))
alarmThread.start ()

print ("Alarm is set for " + alarmTime)
