"""
countdownTimer.py
Ashley Ung 

This program functions as a countdown timer. 
"""

import tkinter as tk
import time

class CountdownTimer:
    def __init__ (self, parent, duration): # a constructor 
        self.parent = parent
        self.duration = duration
        self.countdownLabel = tk.Label (self.parent, text = self.formatTime (self.duration))
        self.countdownLabel.pack ()
        self.updateCountdown ()
    
    def formatTime (self, seconds):
        """Format the time as MM:SS"""
        mins, secs = divmod (seconds, 60)
        return '{:02d}:{:02d}'.format(mins, secs)

    def updateCountdown(self):
        self.duration -= 1 # Update the countdown display and schedule another update in 1 second 
        if self.duration < 0:
            self.countdownLabel.configure (text = 'Countdown Complete!')
        else:
            self.countdownLabel.configure (text = self.formatTime (self.duration))
            self.parent.after (1000, self.updateCountdown)

root = tk.Tk () # Create the root window
root.title ('Countdown Timer')

timer = CountdownTimer (root, 10) # Create the countdown timer & countdown from 10 seconds

root.mainloop () # Runs the GUI loop event
