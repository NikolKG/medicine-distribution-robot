######################### Importing modules #########################
from main_code.homing import *
from main_code.moduless import  *
from main_code.confi import *

######################### calibrate_A function #########################
# Function for A axis calibration
def calibrate_A():
    homing()
    step_count = 0
    GPIO.output(DIR_A, not MOTOR_A_DIR_CW)
    # counting the steps between minimum limit to maximum limit of the axis
    while True:
        i = GPIO.input(endstop_A_Pin)  # read status of pin/port and assign to variable i
        GPIO.output(STEP_A, GPIO.HIGH)
        sleep(delay_home_A)
        GPIO.output(STEP_A, GPIO.LOW)
        sleep(delay_home_A)
        step_count = step_count + 1
        if (i == 1):
            break
    # calculate the number of steps between cells
    Motor_A_steppercell = step_count / No_Of_Cells_A
    print("The step count is:", step_count)
    print("The step per cell is:", Motor_A_steppercell)
    Home_A()
    return (Motor_A_steppercell)


######################### calibrate_A function #########################
# Function for Z axis calibration
def calibrate_Z():
    homing()

    step_count = 0
    GPIO.output(DIR_Z, not MOTOR_Z_DIR_CW)
    # counting the steps between minimum limit to maximum limit of the axis
    while True:
        i = GPIO.input(endstop_Z_Pin)  # read status of pin/port and assign to variable i
        GPIO.output(STEP_Z, GPIO.HIGH)
        sleep(delay_home_Z)
        GPIO.output(STEP_Z, GPIO.LOW)
        sleep(delay_home_Z)
        step_count = step_count + 1
        if (i == 1):
            break
    # calculate the number of steps between cells
    Motor_Z_steppercell = step_count / No_Of_Cells_Z
    print("The step count is:", step_count)
    print("The step per cell is:", Motor_Z_steppercell)
    Home_Z()
    return (Motor_Z_steppercell)


######################### Testing the Calibration #########################
if __name__ == "__main__":
    calibrate_A()