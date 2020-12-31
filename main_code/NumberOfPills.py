######################### Importing modules #########################
from main_code.moduless import  *
from main_code.confi import *


######################### take_pic_from_cam function #########################
# This function taking a picture from the camera
def take_pic_from_cam():
    cam = cv2.VideoCapture(1)  # 0 -> index of camera
    s, img = cam.read()
    return img


######################### save_pic_to_path function #########################
# This function save the picture that taken
def save_pic_to_path(img, path):
    cv2.imwrite(path, img)


######################### checking_number_of_pills function #########################
# This function count the number of pills in the picture
def checking_number_of_pills():
    save_pic_to_path(take_pic_from_cam(), "resuorses/Temp1.jpg")
    #{
        #}
    NumOfPills = 0
    return (NumOfPills)