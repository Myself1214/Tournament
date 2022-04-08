#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

my_dict = {}
participants = 0
participant_slots =[]
main_condition = False

print('Welcome to R us Tournament')
print('==========================')


            
def sign_up():
    print('Participant Sign Up')
    print('===================')
    condition = False
    while condition is False:
        name = input('Please enter participant name: ')
        if not name.isalpha():
            print('That was not valid name. Please try again')
        else:
            condition = True
            
    condition2 = False
    while condition2 is False:
        slot = input(f'Desired starting slot # [0-{participants}]: ')
        if not slot.isnumeric():
            print('That was not a number. Please input starting slot number')
        else:
            if int(slot) > participants:
                print('You input is out of range of available slots')
            elif int(slot) in participant_slots:
                print(f'Slot number {slot} is filled. Please try again')
            else:
                participant_slots.append(int(slot))
                print('Success')
                print(f'{name} is signed up in starting slot #{slot}')
                my_dict[name]=int(slot)
                condition2 = True
                
def cancel():
    condition3 = False
    while condition3 is False:
        print('Participant Cancellation')
        print('========================')
        condition = False
        while condition is False:
            cancel_slot = input(f'Starting slot#[0-{participants}]: ')
            if not cancel_slot.isnumeric():
                print('That was not a number. Please input a number')
            elif int(cancel_slot) > participants:
                print('That number is out of available slot range')
            else:
                cancel_slot = int(cancel_slot)
                condition = True

        condition2 = False
        while condition2 is False:
            cancel_name = input('Participant name: ')
            if not cancel_name.isalpha():
                print('That was not a valid name. Please enter a valid name')
            elif (cancel_name, cancel_slot) not in my_dict.items():
                print(f'Error. {cancel_name} is not in starting slot {cancel_slot}')
                condition2 = True
            elif (cancel_name, cancel_slot) in my_dict.items():
                print('Success')
                my_dict.pop(cancel_name)
                print(f'{cancel_name} has been cancelled from starting slot #{cancel_slot}')
                condition2 = True
                condition3 = True
                
                  
def view():
    print('View Participants')
    print('=================')
    condition = False
    while condition is False:
        slot_view = input(f'Starting slot #[0-{participants}]: ')
        print()
        if not slot_view.isnumeric():
            print('That was not a number. Please input slot number to view')
        elif int(slot_view) > participants:
            print('That number is out of available slot range. Try again')
        elif int(slot_view) not in my_dict.values():
            print('None')
        else:
            print('Starting Slot: Participant')
            new_list = list(my_dict.items())
            for i in new_list:
                print(f'{i[1]}: {i[0]}')
            condition = True
            

def save():
    print('Save changes')
    print('============')
    condition = False
    while condition is False:
        save_change = input('Save your changes to csv? Y/N').upper()
        if not save_change.isalpha():
            print('Please choose Y or N. Try again')
        elif save_change == 'N':
            condition = True
        elif save_change == 'Y':
            field_names=['Participant', 'Starting Slot']
            with open('ParticipantSlot.csv', 'w') as file:
                writer=csv.writer(file)
                writer.writerows(my_dict)
                print('Changes saved')
                condition = True
                  

def exit():
    print('Exit')
    print('=====')
    print('Any unsaved changes will be lost.')
    global main_condition
    condition = False
    while condition is False:
        exit = input('Are you sure you want to exit? Y/N').upper()
        if not exit.isalpha():
            print('That was not valid input. Please try again')
        elif exit == 'N':
            condition = True
        else:
            main_condition = True
            condition = True
            
            
def participant_number():
    global participants
    global main_condition
    condition = False
    while condition is False:
        participant_number = input('Enter number of desired participants: ')
        if not participant_number.isnumeric():
            print('Your input was not a number. Please enter a number')
        else:
            print(f'There are {participant_number} participant slots that are open for sign-ups')
            print()
            participants+=int(participant_number)
            condition = True    

                  

    print('Participant Menu')
    print('================')
    print('1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Save Changes\n5. Exit')
    condition = False
    while main_condition is False:
        menu_choice = input('Choose your menu number: ')
        print()
        if not menu_choice.isnumeric():
            print('That was not a number. Please enter a number from menu')
        else: 
            if menu_choice == '1':
                sign_up()
            elif menu_choice == '2':
                cancel()
            elif menu_choice == '3':
                view()
            elif menu_choice == '4':
                save()
            elif menu_choice == '5':
                exit()
            else:
                print('Please make a selection between 1 to 5')
                
            
    

participant_number()


# In[ ]:




