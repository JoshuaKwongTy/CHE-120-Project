# Names: Joshua Kwong (20938611), Aydan Polkinghorne (20964201), Denis Tyan (20929619)

import random


def getSecretNum(NUM_DIGITS):
    # Returns a string of unique random digits that is NUM_DIGITS long
    numbers = list(range(10))
    random.shuffle(numbers)

    ">>> with the use of the random module we are able to generate a random number that is NUM_DIGITS long"

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    ">>> Takes the digits from the shuffled numbers, then adds it to a blank list"

    return secretNum


def getClues(guess, secretNum):
    # Returns a string with the Pico, Fermi, & Bagels clues to the user
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
    # Returns True if num is a string of only digits. Otherwise returns False.
    if num == "":
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True


def output(k):  # Where the main game takes place for single player
    MAX_GUESS = k[0]  # takes the max_guess value from list k, which was formed in the intro function
    NUM_DIGITS = k[1]  # takes the num_digits value from list k
    while True:
        secretNum = getSecretNum(NUM_DIGITS)
        print("I have thought of a number. You have %s guesses to get it." % (MAX_GUESS))

        guessesTaken = 1
        while guessesTaken <= MAX_GUESS:
            # when guesses taken is lower than or equal to max guesses
            guess = ""
            while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
                print("Guess #%s: " % guessesTaken)  # Each guess prints out which guess you are on
                guess = input()  # takes the input from user for their guess
                if not isOnlyDigits(guess):  # if user does not input a digit repeat the question
                    print("Please enter in a valid input")
                elif len(guess) != NUM_DIGITS:
                    # makes sure that the length of guess is equal to the length num digits
                    print(f"Please enter in {NUM_DIGITS} digits in your guess please.")

            print(getClues(guess, secretNum))  # prints the clues
            guessesTaken += 1  # adds one to guesses taken

            if guess == secretNum:  # if guess is equal to the "secretnumber" break the loop and "win"
                break
            if guessesTaken > MAX_GUESS:  # if guesses taken is more than the max guesses, you lose the game
                print("You ran out of guesses. The answer was %s" % secretNum)
        print("Do you want to play again?(yes or no)")
        if input().lower().startswith('y'):
            intro()
        break


def intro():  # Allows for the user to choose their gamemode
    while True:
        MAX_GUESS = input("How many guesses would you like? (The recommended number of guesses is 10) ")
        if MAX_GUESS.isdigit() is True:  # makes sure that the input is a digit
            MAX_GUESS = int(MAX_GUESS)  # makes MAX_GUESS have the type int instead of the type string
            NUM_DIGITS = input(
                "How many digits long would you like the number to guess be? (The recommended length is 3) ")
            if NUM_DIGITS.isdigit() == True:
                NUM_DIGITS = int(NUM_DIGITS)  # makes NUM_DIGITS have type int instead of type string
                print(f"Are you fine with your choices, Guesses: {MAX_GUESS}, Numbers to guess: {NUM_DIGITS}")
                if input().lower().startswith('y'):  # makes sure that the user is happy with their current settings
                    k = [MAX_GUESS] + [NUM_DIGITS]  # makes k be a list of MAX_GUESS and NUM_DIGITS
                    output(k)  # Calls the output function with the variable k
                    break
