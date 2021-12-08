import random

NUM_DIGITS = 3
MAX_GUESS = 10


# Denis Tyan (DT)
def getSecretNum():
    # Returns a string of unique random digits that is NUM_DIGITS long
    numbers = list(range(10))  # Creates a list with (0,1,2,3,4,5,6,7,8,9)
    random.shuffle(numbers)  # Randomizes numbers list, into random order
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])  # Takes first three digits of the new list and makes it the secret number.
    return secretNum


def getClues(guess, secretNum):
    # Returns a string with the Pico, Fermi, & Bagels clues to the user
    if guess == secretNum:
        return 'You got it'  # If the guess is the same as the secretNum, it ends the loop.
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append(
                'Fermi')  # If the guess has a number that is correct, AND in the correct index, it returns fermi.


        # Aydan Polkinghorne(AP)
        elif guess[i] in secretNum:  # if the guess has the correct number but different index return Pico
            clues.append('Pico')
    if len(clues) == 0:  # if there are zero clues added to the clues string, it return Bagels.
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)


def isOnlyDigits(num):
    # Retures true if the number in the guess is only digits within the range of 0-10. If it is not return false
    if num == "":  # Checks if the input is blank and returns false
        return False
    for i in num:  # Checks if the number is within the range of 0-10
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True


print(
    "I am thinking of a %s-digit number. Try to guess what it is." % (NUM_DIGITS))  # Prints out a statment for the game
print("The clues I give are...")  # Starts the explanation of the clues
print("When I say: That means:")
print("Bagels" + " " * 5 + "None of the digits is correct.")  # Explains what bagels mean
print("Pico" + " " * 5 + "One digit is correct but in the wrong position.")  # Explains what Pico means
print("Fermi" + " " * 5 + "One digit is correct and in the right position.")  # Explains what Fermi means

# Joshua Kwong (JK)
while True:  # General loop to keep the game running
    # By default, the loop will keep running until there is a "break" statement
    secretNum = getSecretNum()  # Gets a random number from the "getSecretNum" function
    print("I have thought up a number. You have %s guesses to get it." % (
        MAX_GUESS))  # User friendly text to tell them how many guesses they have

    guessesTaken = 1  # The user always starts off with the first guess, so guessesTaken always starts off with 1
    while guessesTaken <= MAX_GUESS:  # Will keep running until the number of guesses the user takes exceeeds the maximum number of guesses
        guess = ""  # Resets the user's guess so they can guess again
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):  # Checks if the user's input is valid
            print("Guess #%s: " % guessesTaken)  # Tells the users what guess their on
            guess = input()  # Lets the user enter in their guess
        print(getClues(guess, secretNum))  # Gives the users clues based on their guess
        guessesTaken += 1  # Adds a guess once the user enters in a guess

        if guess == secretNum:
            break  # If the user's guess is the answer, it breaks the whole loop as there is no point in entering other guesses
        if guessesTaken > MAX_GUESS:
            print(
                "You ran out of guesses. The answer was %s" % secretNum)  # If the user runs out of guesses, it will output this user friendly text
    print("Do you want to play again?(yes or no)")  # Asks the user if they want to play again
    if not input().lower().startswith('y'):
        break  # If the user's input does not start with a y, then it breaks out of the general loop and ends the game
        # Anything else means that the user's input starts with a y and it will run the code again


