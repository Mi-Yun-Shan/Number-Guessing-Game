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
