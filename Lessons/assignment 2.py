"""
Author : Muhammad Hashim
Student Number: 752451
Due date : 21 March 2025
"""

"""
Program : Number Guessing Game
Description : A game where the user tries to guess a randomly generated number between 1 and 100 within 6 tries.
VARIABLE DICTIONARY :
correct_numb (int) = Stores the randomly generated number between 1 and 100.
guesscount (int) = Tracks the number of guesses the user has made.
max_tries (int) = The maximum number of guesses allowed (6).
u_guess (int) = Stores the number input by the user on each guess.
"""


import random

# Initialize the game
correct_numb = random.randint(1, 100)  
# Randomly generate a number between 1 and 100 and assign it to 'correct_numb'

guesscount = 0  
# Set the initial guess count to 0 to track how many guesses the user has made

# Print introduction to the game
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")

# Loop for user guesses
while guesscount < 6:
    guesscount += 1  
    # Increment the guess count by 1 with each iteration

    u_guess = int(input("Guess #%d: " % guesscount))  
    # Prompt the user to input their guess and convert it to an integer

    # Check if the guess is correct, too high, or too low
    if u_guess < correct_numb:
        print("Higher!")  
        # If the guess is too high, prompt the user to guess a higher number
    elif u_guess > correct_numb:
        print("Lower!")  
        # If the guess is too low, prompt the user to guess a lower number
    else:
        print("You guessed right!")  
        # If the guess is correct, notify the user they won
        guesscount = 7  
        # End the game early by setting guesscount to 7

# After the loop ends, check if the user failed to guess the number
if u_guess != correct_numb:
    print("Sorry: you are out of guesses! The answer was %d. Better luck next time!" % correct_numb)
    # If the guess is still wrong after 6 attempts, inform the user and show the correct number
