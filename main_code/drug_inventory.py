######################### Importing modules #########################
from main_code.moduless import  *
from main_code.confi import *


######################### load_json function #########################
# Function for open json file
def load_json(file_name, path="resources/"):
    with open(path + file_name, 'r') as json_file:
        return json.load(json_file)


######################### load_json_file function #########################
# Function for loading the json file into dictionary variable
def load_json_file():
    # load json file intro dict variable
    drugs_list = load_json("drugs_list.json", "./resuorses/")  # load json function return dict
    return drugs_list


######################### View_drug_inventory function #########################
# Function for display the drug inventory
def View_drug_inventory():
    drugs_list = load_json_file()
    for drug in drugs_list:
        print(drug, ")", "drug name:", drugs_list[drug]['drug_name'], '\n', '   ', "invetory:", drugs_list[drug]['invetory'], '\n')


if __name__ == "__main__":
    View_drug_inventory()
