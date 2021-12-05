import random
import time

NUM_DIGITS = 3
MAX_GUESS = 0


def getSecretNum():
    #Returns a string of unique random digits that is NUM_DIGITS long
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess,secretNum):
    #Returns a string with the Pico, Fermi, & Bagels clues to the user
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)


def isOnlyDigits(num):
    #Returns True if num is a string of only digits. Otherwise returns False.
    if num == "":
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True


def tries_input():
    # Returns the number of guesses the user enters if the input is valid
    while True:
        max_guess_input = input("How many tries do you want for your game (limit of 15)?: ")
        if max_guess_input.isdigit():  # Checks if the input is an integer input
            if 0 < int(max_guess_input) <= 15:
                MAX_GUESS = int(max_guess_input)
                return MAX_GUESS
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")


def gamemode_type():
    # Returns the number of seconds the user has when the user has chosen a valid game mode
    while True:
        gamemode_input = input("Enter in the number associated with the gamemode you want to play (1,2,3): ")
        if gamemode_input.isdigit():
            if gamemode_input == "1":
                return 15
            elif gamemode_input == "2":
                return 50
            elif gamemode_input == "3":
                return 75
            else:
                print("Invalid input!")
        else:
            print("Invalid input")


def yes_or_no():
    # Returns if the user said yes or no
    while True:
        user_continue = input("Yes or no?: ").lower()
        if user_continue == "yes":
            return user_continue
        elif user_continue == "no":
            return user_continue
        else:
            print("Invalid input!")


def guess_input(guesses):
    # Returns the user's guess if their input is valid
    guess = ""
    while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
        guess = input(f"Guess #{guesses + 1}: ")
        if not isOnlyDigits(guess):
            print("Please enter in a valid input!")
        elif len(guess) != NUM_DIGITS:
            print(f"Please enter in {NUM_DIGITS} digits in your guess!")
    return guess


def output():
    # Main game
    print("Welcome to the mulitplayer mode where you can play against your friends!") # User friendly text
    print('''Instructions:
- You and another person will go head to head and guess the chosen number. Whoever gets it first wins.
- There will a timer associated with each user, so better put in those guesses quick!
- If the timer runs out for one player, that player is out and the other player wins
- You have a set amount of tries and you can enter in how many tries both of you have''')
    play_again = True
    while play_again is True: # Main big loop that contains the whole game . Will be used at the end to see if the user wants to play again
        loop = True
        while loop: # Loop to keep running if the user is unhappy with their settings
            MAX_GUESS = tries_input()
            print("-" *10)

            print('''What gamemode would you like?
1. Blitz (15 seconds total)
2. Normal (50 seconds total)
3. Casual (75 seconds total)''')
            timer1 = 0
            timer2 = 0
            timer = gamemode_type()
            timer1 = timer
            timer2 = timer

            print("-" *10)

            print(f'''Your current game settings:
Number of guesses: {MAX_GUESS}
Time To Guess: {timer1} seconds
Are you happy with these settings?''')
            user_continue = yes_or_no()
            if user_continue == "yes":
                loop = False
            elif user_continue == "no":
                print("Bringing you to the beginning...")
                time.sleep(1)
                print("-" * 10)

        print("-" * 10)
        secret_num = getSecretNum()
        print(f"I am thinking of a {NUM_DIGITS}-digit number, meaning your guesses must also be {NUM_DIGITS} digits. Try to guess what it is.")
        time_input = time.perf_counter() # Keeps track of how long the user takes to enter in their settings
        win = True
        player1_win = False
        player2_win = False
        actual_time1 = 0
        actual_time2 = 0
        time_before = 0
        guesses1 = 0
        guesses2 = 0
        while win: # Checks if one player wins, if they did then it will exit out of this loop
            while guesses1 < MAX_GUESS and player1_win is False and actual_time1 <= timer1: # Player 1 Turn loop
                print("-" * 10)
                print("Player 1 Turn")
                guess = guess_input(guesses1)
                actual_time1 = actual_time1 + (time.perf_counter() - time_input - time_before) # Checks the time it took for the user to input their guess
                time_before = time.perf_counter() - time_input # Saves the time when the user is done inputting their guess (minus their input time)
                if actual_time1 <= timer1:
                    print(getClues(guess, secret_num)) # Gives the clues to the user
                    guesses1 += 1
                    if guess == secret_num:
                        player1_win = True
                        break
                    elif guesses1 >= MAX_GUESS:
                        print("You have no more tries")
                        guesses1 += 1 # Adds a guess to break player 1 loop
                        break
                    print("Remaining time: " + str(round(timer1 - actual_time1, 2)) + "s")
                    if guesses2 <= MAX_GUESS and actual_time2 <= timer2:
                        break # Breaks player 1 loop to go to player 2 loop
                        # If player 2 can no longer guess (surpassing guesses/time), then it will keep running player 1 loop
                else:
                    print("You ran out of time and therefore, your last input was counted as invalid.")
                    guesses1 = 16 # To break the win loop in later code
                    break

            while guesses2 < MAX_GUESS and player2_win is False and actual_time2 <= timer2: # Player 2 loop (Same as player 1 loop but for player 2)
                if player1_win: # If player 1 already won, there's no point in running this loop
                    break
                print("-" * 10)
                print("Player 2 Turn")
                guess = guess_input(guesses2)
                actual_time2 = actual_time2 + (time.perf_counter() - time_input - time_before) # Checks the time it took for the user to input their guess
                time_before = time.perf_counter() - time_input # Saves the time when the user is done inputting their guess (minus their input time)
                if actual_time2 <= timer2:
                    print(getClues(guess, secret_num)) # Gives the clues to the user
                    guesses2 += 1
                    if guess == secret_num:
                        player2_win = True
                        break
                    elif guesses2 >= MAX_GUESS:
                        print("You have no more tries!")
                        guesses2 += 1 # Adds a guess to break player 1 loop
                        break
                    print("Time Remaining: " + str(round(timer2 - actual_time2, 2)) + "s")
                    if guesses1 <= MAX_GUESS and actual_time1 <= timer1:
                        break # Breaks player 2 loop to go to player 1 loop
                        # If player 1 can no longer guess (surpassing guesses/time), then it will keep running player 2 loop
                else:
                    print("You have ran out of time and therefore, your last input was counted as invalid.")
                    guesses2 = 16 # To break the win loop in later code
            if player1_win is True or player2_win is True:
                break # If one person wins, it breaks the whole loop as there is no point running again
            elif guesses1 >= MAX_GUESS and guesses2 >= MAX_GUESS:
                break # This means that they both lost, so we do not need to run it again

        print("-" * 10)
        if player1_win:
            print("Congratulations! Player 1 has won!")
        elif player2_win:
            print("Congratulations! Player 2 has won!")
        else:
            print("No one has won. The number was " + str(secret_num))
        print("-" * 10)
        print("Do you want to play again?")
        answer = yes_or_no()
        if answer == "no":
            play_again = False # If the user doesn't want to play again, it breaks the big loop
