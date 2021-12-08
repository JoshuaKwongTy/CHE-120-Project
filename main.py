# Names: Joshua Kwong (20938611), Aydan Polkinghorne (20964201), Denis Tyan (20929619)

import multiplayer
import singleplayer

PROJECT_NAME = "Bagels"
run = True
#Assignment of variables to create a while loop which helps with making sure only valid inputs are entered.

print(f'''Welcome to {PROJECT_NAME}!
Created by: Joshua Kwong, Aydan Polkinghorne, and Denis Tyan.''')
print("-"*10)
#Title of game, and the print("-"*10) statement adds a clarifying dotted line.
while run:
    print("Main Menu:")
    print('''1. Instructions for Bagels!
2. Singleplayer
3. Multiplayer''')
#Presents the main menu to the player
    user_input = input("Type in the corresponding number of your choice (1,2,3, or exit): ").lower()
    if user_input == "1" or user_input == "2" or user_input == "3" or user_input == "exit":
        #Depending on input, the code will direct you to one of the choices.
        if user_input == "1":
            print("-"*10)
            print('''The computer will generate a random number and it is your job to guess what the number is by inputting a certain amount of digits.
The amount of digits will be specified. Once you input those numbers, the computer will tell you if you inputted the correct
numbers in the right place. However, they will tell you by saying three phrases:
Bagles: None of the digits is correct
Pico: One digit is correct but in the wrong position
Fermi: One digit is correct and in the right position''')
            done = input("Enter in anything when you're done reading: ")
            print("-" * 10)
        elif user_input == "2":
            print("-" * 10)
            singleplayer.intro()
            #This runs singleplayer if the player chooses 2 as their option.
            print("-" * 10)
        elif user_input == "3":
            print("-" * 10)
            multiplayer.output()
            #This runs multiplayer if the player chooses 3 as their option.
            print("-" * 10)
        elif user_input == "exit":
            run = False
            #This changes the variable 'run' to False, which ends the processing of the code.
    else:
        print("Invalid input!")
        print("-" * 10)
        #This message will show up if anything other than 1,2,3, or exit are inputted, and the 'run' loop restarts.
print("Thanks for playing!")
