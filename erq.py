#escape room questions
import time
#allows timer function
import ctypes
#allows for pop out box 
import webbrowser
#using imported modules to add extra functionality, the modules may not have a counter part in java and this causes an issue with compatability
ctypes.windll.user32.MessageBoxW(0, "Welcome, this is an very early build of a set of questions made specifically for an escape room" , "intro", 1)
time.sleep(1)
