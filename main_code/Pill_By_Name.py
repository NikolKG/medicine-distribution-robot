######################### Importing modules #########################
from main_code.moduless import *
from main_code.confi import *
from main_code.pill_out import *


######################### load_json function #########################
# Function for open json file
def load_json(file_name, path="resources/"):
    with open(path + file_name, 'r') as json_file:
        return json.load(json_file)


######################### load_json_file function #########################
# Function for loading the json file into dict variable
def load_json_file():
    # load json file intro dict variable
    patients_list = load_json("patients_list.json", "./resuorses/")  # load json function return dict
    return patients_list


######################### pill_by_number function #########################
# Function for loading patient information
def pill_by_number(selected_patient, current_position):
    patients_list = load_json_file()
    selected_patient_str = str(selected_patient)
    drug_amount = len(patients_list[selected_patient_str]['drugs_list'])
    print(drug_amount)
    # loop over dict keys patient list drugs_list
    for drug_number in range(1, drug_amount+1):
        # get drug name and quantity into variables
        drug_name = patients_list[selected_patient_str]['drugs_list'][str(drug_number)]['drug_name']
        drug_sum = patients_list[selected_patient_str]['drugs_list'][str(drug_number)]['amount']
        # collecting pills by name and quantity
        pill_out(drug_name, drug_sum, current_position)
    go_to(0, 0, current_position)


######################### print_patients_list function #########################
# Function for printing patient list
def print_patients_list():
    patients_list = load_json_file()
    # loop over dict keys patient list drugs_list
    for patient in patients_list:
        print(patient, ")", patients_list[patient]['first_name'], patients_list[patient]['last_name'],
              patients_list[patient]['id'])


######################### pill_by_name function #########################
# Function for selcting patient
def pill_by_name(current_position):
    print_patients_list()
    selected_patient = int(input("What is the patients number?"))
    # print(selected_patient)
    pill_by_number(selected_patient, current_position)


if __name__ == "__main__":
    current_position = [0, 0]
    pill_by_name(current_position)
