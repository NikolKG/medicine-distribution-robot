######################### Importing modules #########################
from main_code.confi import *
from main_code.motor_status import *


######################### Function for servo 1 homing #########################
def Home_Servo_1():
    Servo_1_SetAngle(0)


######################### Function for A axis homing #########################
def Home_A():
   # This loop move the axis in negative direction until the sensor is triggered
    while True:
        GPIO.output(DIR_A, MOTOR_A_DIR_CW)
        inA = GPIO.input(endstop_A_Pin)  # Read status of "endstop A" and assign to variable inA
        if (inA == 1):
            break
        GPIO.output(STEP_A, GPIO.HIGH)
        sleep(delay_home_A)
        GPIO.output(STEP_A, GPIO.LOW)
        sleep(delay_home_A)

   # This loop move the axis in positive direction until the sensor is untriggered
    while (inA == 1):
        GPIO.output(DIR_A, not MOTOR_A_DIR_CW)
        inA = GPIO.input(endstop_A_Pin)
        GPIO.output(STEP_A, GPIO.HIGH)
        sleep(delay_home_A)
        GPIO.output(STEP_A, GPIO.LOW)
        sleep(delay_home_A)

    current_position[1] = 0      # Reset the current position to 0
    return current_position[1]


######################### Function for A axis homing #########################
def Home_Z():
    # This loop move the axis in negative direction until the sensor is triggered
    while True:
        inZ = GPIO.input(endstop_Z_Pin)  # Read status of "endstop Z" and assign to variable i
        if (inZ == 1):
            break
        GPIO.output(DIR_Z, MOTOR_Z_DIR_CW)
        GPIO.output(STEP_Z, GPIO.HIGH)
        sleep(delay_home_Z)
        GPIO.output(STEP_Z, GPIO.LOW)
        sleep(delay_home_Z)

    # This loop move the axis in positive direction until the sensor is untriggered
    while (inZ == 1):
        GPIO.output(DIR_Z, not MOTOR_Z_DIR_CW)
        inZ = GPIO.input(endstop_Z_Pin)
        GPIO.output(STEP_Z, GPIO.HIGH)
        sleep(delay_home_Z)
        GPIO.output(STEP_Z, GPIO.LOW)
        sleep(delay_home_Z)

    current_position[0] = 0     # Reset the current position to 0
    return current_position[0]


######################### Homing function #########################
def homing():
    # Home_Servo_1()
    enable_motors()
    current_position[1] = Home_A()
    current_position[0] = Home_Z()
    return current_position


######################### Testing the Homing function #########################
if __name__ == "__main__":
    homing()
    #Home_Servo_1()
    #Home_A()
    #Home_Z()
