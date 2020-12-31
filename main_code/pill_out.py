######################### Importing modules #########################
from main_code.moduless import *
from main_code.confi import *
from main_code.GoTo import *
from main_code.SERVO_ANGLE import *
from pill_detector import *


######################### load_json function #########################
# Function for open json file
def load_json(file_name, path="resources/"):
    with open(path + file_name, 'r') as json_file:
        return json.load(json_file)


######################### load_json_file function #########################
# Function for loading the json file into dict variable
def load_json_file():
    drugs_list = load_json("drugs_list.json", "./resuorses/")  # load json function return dict
    return drugs_list


######################### pill_out function #########################
# Function for collecting pills by name and quantity
def pill_out(drug_name, drug_quantity, current_position):
    drugs_list = load_json_file()
    for drug in drugs_list:
        # search for a drug in drugs list
        if drug_name == (drugs_list[drug]['drug_name']):
            # get drug location into variables
            destinastion_A = (drugs_list[drug]['capsul_location_A'])
            destinastion_Z = (drugs_list[drug]['capsul_location_Z'])
            # go to drug location
            go_to(destinastion_Z, destinastion_A, current_position)
            # loop for collecting pills by quantity
            for drug_num in range(1, drug_quantity + 1):
                # print(amount_of_pills())
                servo_1_out()
                # inventory update after collecting pill
                new_inventory = drugs_list[drug]['invetory']
                new_inventory -= 1
                drugs_list[drug]['invetory'] = new_inventory
                sleep(2)
                print(new_inventory)
                # Identifies the number of pills in cup using image recognition
                print(amount_of_pills())


if __name__ == "__main__":
    current_position[0] = 0
    current_position[1] = 0
    pill_out('Erythromycin', 1, current_position)
