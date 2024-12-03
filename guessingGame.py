# imports
import random

# global variables
numToGuess = random.randint(1, 100)

def gameplayLoop(guessesMade, loopLimit): # gameplay loop
    tries = guessesMade # count of guesses made

    while tries <= loopLimit: # game loop

        # validation
        try:
            guess = int(input(f"Guess {tries}: "))
        except ValueError:
            print("Please enter an integer\n")
            tries += 1
            gameplayLoop(tries)

        # selection
        if guess > numToGuess:
            print(f"Too high!, The number is less than {guess}.\n")
            tries += 1
        elif guess < numToGuess:
            print(f"Too low!, The number is greater than {guess}.\n")
            tries += 1
        else:
            # win condition
            print("You guessed the correct number!\n")
            menu()

    # lose condition
    print("Better luck next time!\n")
    menu()

def menu(): # menu function used in main() to produce the game-mode selection

    print("Difficulty Selection:")
    print("1. Easy (10 Guesses)")
    print("2. Medium (5 Guesses)")
    print("3. Hard (3 Guesses)")
    print("0. Exit\n")

    # input validation
    try:
        difficultyChoice = int(input("Enter your choice: \n"))
    except:
        print("Invalid input\n")
        menu()


    # selection
    if difficultyChoice == 1:
        gameplayLoop(1, 10)
    elif difficultyChoice == 2:
        gameplayLoop(1, 5)
    elif difficultyChoice == 3:
        gameplayLoop(1, 3)
    else:
        print("Input out of range")
        menu()

def main():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100... Can you guess which one? \n")
    menu()

main()