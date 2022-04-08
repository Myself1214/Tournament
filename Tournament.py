#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

#declare variables
my_dict = {}
participants = 0
participant_slots =[]
main_condition = False

#print header
print('Welcome to R us Tournament')
print('==========================')


#Function for Sign up            
def sign_up():
    print('Participant Sign Up')
    print('===================')
    condition = False
    while condition is False:                          #input check for alpha input
        name = input('Please enter participant name: ')
        if not name.isalpha():
            print('That was not valid name. Please try again')
        else:
            condition = True
            
    condition2 = False
    while condition2 is False:                          #input check for numeric input
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
                my_dict[name]=int(slot)                  #adding name and value to dictionary
                condition2 = True

#funcrion for sign up cancellation
def cancel():
    condition3 = False
    while condition3 is False:                          
        print('Participant Cancellation')
        print('========================')
        condition = False
        while condition is False:                       # input check for numeric input
            cancel_slot = input(f'Starting slot#[0-{participants}]: ')
            if not cancel_slot.isnumeric():
                print('That was not a number. Please input a number')
            elif int(cancel_slot) > participants:
                print('That number is out of available slot range')
            else:
                cancel_slot = int(cancel_slot)
                condition = True

        condition2 = False
        while condition2 is False:                        #input check for ailpha input
            cancel_name = input('Participant name: ')
            if not cancel_name.isalpha():          
                print('That was not a valid name. Please enter a valid name')
            elif (cancel_name, cancel_slot) not in my_dict.items():  #name or value mismatch check
                print(f'Error. {cancel_name} is not in starting slot {cancel_slot}')
                condition2 = True
            elif (cancel_name, cancel_slot) in my_dict.items():  #removing participant
                print('Success')
                my_dict.pop(cancel_name)
                print(f'{cancel_name} has been cancelled from starting slot #{cancel_slot}')
                condition2 = True
                condition3 = True
                
#function for participant view                  
def view():
    print('View Participants')
    print('=================')
    condition = False
    while condition is False:                                       # input check for numeric input
        slot_view = input(f'Starting slot #[0-{participants}]: ')
        print()
        if not slot_view.isnumeric():
            print('That was not a number. Please input slot number to view')
        elif int(slot_view) > participants:
            print('That number is out of available slot range. Try again')
        elif int(slot_view) not in my_dict.values():                 #eliminationg mismatch
            print('None')
        else:
            print('Starting Slot: Participant')    #printing participants
            new_list = list(my_dict.items())
            for i in new_list:
                print(f'{i[1]}: {i[0]}')
            condition = True
            
#function to save changes
def save():
    print('Save changes')
    print('============')
    condition = False
    while condition is False: 
        save_change = input('Save your changes to csv? Y/N').upper()
        if not save_change.isalpha():                                 ##input check for ailpha input
            print('Please choose Y or N. Try again')
        elif save_change == 'N':
            condition = True
        elif save_change == 'Y':
            with open('ParticipantSlot.csv', 'w') as file:             #creating file
                writer=csv.writer(file)                                #writing to file
                writer.writerows(my_dict)
                print('Changes saved')
                condition = True
                  
#function to exit
def exit():
    print('Exit')
    print('=====')
    print('Any unsaved changes will be lost.')
    global main_condition
    condition = False
    while condition is False:                                         #check input for alpha input
        exit = input('Are you sure you want to exit? Y/N').upper()
        if not exit.isalpha():
            print('That was not valid input. Please try again')
        elif exit == 'N':
            condition = True
        else:
            main_condition = True                                      #exiting game
            condition = True
            
#main code            
def participant_number():
    global participants
    global main_condition
    condition = False
    while condition is False:                                          #getting number of participants
        participant_number = input('Enter number of desired participants: ')
        if not participant_number.isnumeric():                         #checking for numeric input
            print('Your input was not a number. Please enter a number')
        else:
            print(f'There are {participant_number} participant slots that are open for sign-ups')
            print()
            participants+=int(participant_number)                       #saving participant number
            condition = True    

                  

    print('Participant Menu')
    print('================')
    print('1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Save Changes\n5. Exit')
    condition = False
    while main_condition is False:
        menu_choice = input('Choose your menu number: ')                 #select menu item
        print()
        if not menu_choice.isnumeric():                                  #check for numeric input
            print('That was not a number. Please enter a number from menu')
        else: 
            if menu_choice == '1':   #references to sign up
                sign_up()
            elif menu_choice == '2':  #references to cancellation of sign up
                cancel()
            elif menu_choice == '3':  #references to participant view
                view()
            elif menu_choice == '4':   #references to saveing changes
                save()
            elif menu_choice == '5':   #references to exiting the tournament
                exit()
            else:
                print('Please make a selection between 1 to 5')
                
            
    

participant_number()  #running the code


# In[ ]:




