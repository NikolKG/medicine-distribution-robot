######################### Importing modules #########################
import os
from main_code.moduless import  *
from main_code.confi import *


from Testing.Testing_Go_To import *

######################### clear_screen function #########################
def clear_screen():
    delay = 0
    sleep(delay)
    print(chr(27) + "[2J")
    os.system('clear')
    tprint("Medicine distribution")

######################### print_menu function #########################
def print_menu(menu_items):
    index = 0
    for menu_item in menu_items:
        if index == 0:
            print(menu_item)
        else:
            print(str(index) + ". for " + menu_item)
        if len(menu_items) - 1 == index:
            print(str(index + 1) + ". for exit.")
        index += 1
    menu_choice = int(input(""))
    return menu_choice

######################### testing_menu_list #########################
testing_menu_list = ['Welcome to Medicine distribution testing: \nplease enter you\'re choice:\n',
                     'testing homing',
                     'testing go to Position',
                     'testing number of pills']

######################### testing_menu function #########################
def testing_menu():
    clear_screen()
    while True:
        menu_choice = print_menu(testing_menu_list)

        if menu_choice == len(testing_menu_list):
            break
        elif menu_choice == 1:
            current_position = homing()

        elif menu_choice == 2:

             Testing_Go_To(current_position)

        elif menu_choice == 3:
            NumOfPills = amount_of_pills()
            print(NumOfPills)

        clear_screen()

######################### operation_menu_list #########################
operation_menu_list = ['Welcome to Medicine distribution operation: \n please enter you\'re choice:\n',
                       'Machine ON',
                       'Patients List',
                       'View drug inventory',
                       'Collect a pill by name',
                       'calibration',
                       'machine off and close',]

######################### operation_menu function #########################
def operation_menu():
    clear_screen()
    while True:
        menu_choice = print_menu(operation_menu_list)

        if menu_choice == len(operation_menu_list):
            break
        elif menu_choice == 1:
            homing()
        elif menu_choice == 2:
            print_patients_list()
        elif menu_choice == 3:
            View_drug_inventory()
        elif menu_choice == 4:
            pill_by_name(current_position)

        elif menu_choice == 5:
            continue
        elif menu_choice == 6:
            disable_motors()
            break

        clear_screen()

######################### main_menu_list #########################
main_menu_list = ['Welcome to Medicine distribution main menu: \n please enter you\'re choice:\n',
                  'testing',
                  'full operation running']

######################### main_menu function #########################
def main_menu():
    clear_screen()
    print("starting application")

    while True:
        menu_choice = print_menu(main_menu_list)

        if menu_choice == len(main_menu_list):
            #homing()
            disable_motors()
            break
        elif menu_choice == 1:
            testing_menu()
        elif menu_choice == 2:
            operation_menu()

        clear_screen()

def main():
    main_menu()

if __name__ == "__main__":
    main()
