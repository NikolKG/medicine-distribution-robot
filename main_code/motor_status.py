######################### Importing modules #########################
#from RPi import GPIO
from main_code.moduless import *

######################### disable_motors function #########################
def disable_motors():
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)

######################### enable_motors function #########################
def enable_motors():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

######################### Testing the Disable_Motors function #########################
if __name__ == "__main__":
    disable_motors()
    #enable_motors()
