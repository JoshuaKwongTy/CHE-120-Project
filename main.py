import multiplayer
import test
import singleplayer

PROJECT_NAME = "Bagels"
run = True

print(f'''Welcome to {PROJECT_NAME}!
Created by: Joshua Kwong, Aydan Polkinghorne, and Denis Tyan.''')
while run:
    print("Select game mode:")
    print('''1. How do you play?
2. Single Player
3. Multiplayer''')
    user_input = input("Type in the number of your choice (1,2,3, or exit): ").lower()
    if user_input == "1" or user_input == "2" or user_input == "3" or user_input == "exit":
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
            test.intro()
            print("-" * 10)
        elif user_input == "3":
            print("-" * 10)
            multiplayer.output()
            print("-" * 10)
        elif user_input == "exit":
            run = False
    else:
        print("Invalid input!")
        print("-" * 10)

print("Thanks for playing!")