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


def gamemode_type():
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
            return -1
    else:
        print("Invalid input")
        return -1


def output():
    print("Welcome to the mulitplayer mode where you can play against your friends!")
    print('''Instructions:
- You and another person will go head to head and guess the chosen number. Whoever gets it first wins.
- There will a timer associated with each user, so better put in those guesses quick!
- If the timer runs out for one player, that player is out and the other player wins
- You have a set amount of tries and you can enter in how many tries both of you have''')
    play_again = True
    while play_again is True:
        loop = True
        while loop:
            run = True
            while run:
                max_guess_input = input("How many tries do you want for your game (limit of 15)?: ")
                if max_guess_input.isdigit(): # Checks if the input is an integer input
                    if 0 < int(max_guess_input) <= 15:
                        MAX_GUESS = int(max_guess_input)
                        run = False
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")

            print("-" *10)

            timer1 = 0
            timer2 = 0
            run = True
            print('''What gamemode would you like?
1. Blitz (15 seconds total)
2. Normal (50 seconds total)
3. Casual (75 seconds total)''')
            while run:
                timer = gamemode_type()
                if timer != -1:
                    run = False
            timer1 = timer
            timer2 = timer

            print("-" *10)

            print(f'''Your current game settings:
Number of guesses: {MAX_GUESS}
Time To Guess: {timer1} seconds
Are you happy with these settings?''')
            run = True
            while run:
                user_continue = input("Yes or no?: ").lower()
                if user_continue == "yes":
                    run = False
                    loop = False
                elif user_continue == "no":
                    run = False
                    print("Bringing you to the beginning...")
                    time.sleep(1)
                    print("-" *10)
                else:
                    print("Invalid input!")

        print("-" * 10)
        secret_num = getSecretNum()
        print(secret_num)
        print(f"I am thinking of a {NUM_DIGITS}-digit number, meaning your guesses must also be {NUM_DIGITS} digits. Try to guess what it is.")
        time_input = time.perf_counter()
        win = True
        player1_loop = True
        player2_loop = True
        player1_win = False
        player2_win = False
        actual_time1 = 0
        actual_time2 = 0
        time_before = 0
        guesses1 = 0
        guesses2 = 0
        while win:
            if player2_win is True:
                win = True
                guesses1 = 16
                guesses2 = 16
            while guesses1 < MAX_GUESS and player1_win is False and actual_time1 <= timer1:
                print("-" * 10)
                print("Player 1 Turn")
                guess = ""
                while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
                    guess = input(f"Guess #{guesses1 + 1}: ")
                    if not isOnlyDigits(guess):
                        print("Please enter in a valid input!")
                    elif len(guess) != NUM_DIGITS:
                        print(f"Please enter in {NUM_DIGITS} digits in your guess!")
                actual_time1 = actual_time1 + (time.perf_counter() - time_input - time_before)
                time_before = time.perf_counter() - time_input
                if actual_time1 <= timer1:
                    print(getClues(guess, secret_num))
                    guesses1 += 1
                    if guess == secret_num:
                        player1_win = True
                        break
                    elif guesses1 >= MAX_GUESS:
                        print("You have no more tries")
                        break
                    print("Remaining time: " + str(timer1 - actual_time1))
                    if guesses2 <= MAX_GUESS and actual_time2 <= 15:
                        break
                else:
                    print("You ran out of time and therefore, your last input was counted as invalid.")
                    guesses1 = 16
                    break

            while guesses2 < MAX_GUESS and player2_win is False and actual_time2 <= timer2:
                if player1_win:
                    break
                print("-" * 10)
                print("Player 2 Turn")
                guess = ""
                while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
                    guess = input(f"Guess #{guesses2 + 1}: ")
                    if not isOnlyDigits(guess):
                        print("Please enter in a valid input!")
                    elif len(guess) != NUM_DIGITS:
                        print(f"Please enter in {NUM_DIGITS} digits in your guess!")
                actual_time2 = actual_time2 + (time.perf_counter() - time_input - time_before)
                time_before = time.perf_counter() - time_input
                if actual_time2 <= timer2:
                    print(getClues(guess, secret_num))
                    guesses2 += 1
                    if guess == secret_num:
                        player2_win = True
                        break
                    elif guesses2 >= MAX_GUESS:
                        print("You have no more tries!")
                        break
                    print("Time Remaining: " + str(timer2 - actual_time2))
                    if guesses1 <= MAX_GUESS:
                        break
                else:
                    print("You have ran out of time and therefore, your last input was counted as invalid.")
                    guesses2 = 16
            if player1_win is True or player2_win is True:
                break
            elif guesses1 >= MAX_GUESS and guesses2 >= MAX_GUESS:
                break

        print("-" * 10)
        if player1_win:
            print("Congratulations! Player 1 has won!")
        elif player2_win:
            print("Congratulations! Player 2 has won!")
        else:
            print("No one has won. The number was " + str(secret_num))
        valid_answer = False
        while valid_answer is False:
            print("Do you want to play again (yes or no)")
            answer = input().lower()
            if answer == "no":
                valid_answer = True
                play_again = False
            elif answer == "yes":
                valid_answer = True
            else:
                print("Invalid answer!")
