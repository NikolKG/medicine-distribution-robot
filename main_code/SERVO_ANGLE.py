######################### Importing modules #########################
from main_code.confi import *
from main_code.moduless import *
from time import sleep


######################### Servo_1_SetAngle function #########################
# This function move the servo to desired angle that move the linear actuator
def Servo_1_SetAngle(angle):
    duty = ((180 - angle) / 18) + 2
    GPIO.output(Servo_1_Pin, True)
    pwm1.ChangeDutyCycle(duty)
    sleep(0.5)
    GPIO.output(Servo_1_Pin, False)
    pwm1.ChangeDutyCycle(0)


######################### servo_1_out function #########################
# This function move the linear actuator all the way out (180) and brings it back inside (0)
def servo_1_out():
    pwm1.start(0)
    delay = 0.5
    Servo_1_SetAngle(0)
    sleep(delay)
    Servo_1_SetAngle(180)
    sleep(delay)
    Servo_1_SetAngle(0)
    sleep(delay)


if __name__ == "__main__":
    servo_1_out()
    #Servo_1_SetAngle(180)
