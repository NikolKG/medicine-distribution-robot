import json


def load_json(file_name, path="resources/"):
    with open(path + file_name, 'r') as json_file:
        return json.load(json_file)


if __name__ == "__main__":
    # load json file intro dict variable
    patients_list = load_json("patients_list.json", "../resuorses/") # load json function return dict

    # print patient list drugs_list in location 1
#    print(patients_list['1']['drugs_list'])

#    print(patients_list.keys())
#    print(patients_list.values())

    # loop over dict keys patient list drugs_list
    for patient in patients_list:
        print(patients_list[patient]['drugs_list'])

    # loop over dict keys patient list drugs_list
    for patient in patients_list.values():
        print(patient['drugs_list'])


'''
    selected_patient = "1"
    print(patients_list[selected_patient]['drugs_list'])
'''