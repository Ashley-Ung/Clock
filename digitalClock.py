"""
digitalClock.py
Ashley Ung 

This program functions as a digital clock GUI.
"""

import tkinter as tk
import time

# Creates a tkinter window
window = tk.Tk ()
window.title ("A Digital Clock!")

# Creates a label to display the time
timeLabel = tk.Label (window, font = ("Times New Roman", 30))
timeLabel.pack ()

# Function to update the time display
def updateTime ():
    currentTime = time.strftime ("%I:%M:%S %p")
    timeLabel.configure (text = currentTime)
    timeLabel.after (1000, updateTime)

# Start the clock
updateTime ()
window.mainloop ()
