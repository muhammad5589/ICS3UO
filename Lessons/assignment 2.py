"""
Author : Muhammad Hashim
Student Number: 752451
Due date : 21 March 2025
Course code: ICS3U0
"""

"""
Program : Number Guessing Game
Description : A game where the user tries to guess a randomly generated number between 1 and 100 within 6 tries.

VARIABLE DICTIONARY :
random_number (int) = Stores the randomly generated number between 1 and 100.
attempts (int) = Tracks the number of guesses the user has made.
max_attempts (int) = The maximum number of guesses allowed (6).
game_over (bool) = A boolean flag to control whether the game loop should continue or end.
user_input (int) = Stores the number input by the user on each guess.
"""


# Import the random module to generate random numbers
import random  

# Initialize the game

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)  

# Initialize attempts count to keep track of how many guesses the user has made
attempts = 0  

# Set the maximum number of attempts allowed
max_attempts = 6  

# Boolean variable to control whether the game loop should continue or end
game_over = False  

# Game Introduction

# Print a welcome message
print("Welcome to the Number Guessing Game!")  

# Explain the game rules
print("I've picked a number between 1 and 100. Can you guess what it is?")  

# Inform the user of the number of attempts they have
print("You have", max_attempts, "attempts to find the correct number. Good luck!")  

# Game loop

# Continue looping as long as the user has attempts left and the game is not over
while attempts < max_attempts and not game_over:  

    # Increment the attempt count by 1 for each guess
    attempts += 1  

    # Prompt the user to enter their guess
    print("Attempt", attempts, ": Enter your guess:")  

    # Get the user's input and convert it to an integer
    user_input = int(input())  

    # Check if the user's guess is higher, lower, or equal to the random number

    # If the guess is higher than the random number
    if user_input > random_number:  
        # Inform the user their guess was too high
        print("Too high! Try a lower number.")  

    # If the guess is lower than the random number
    elif user_input < random_number:  
        # Inform the user their guess was too low
        print("Too low! Try a higher number.")  

    # If the guess is correct
    else:  
        # Congratulate the user
        print("Congratulations! You guessed the number in", attempts, "tries! 🎉")  

        # Set game_over to True to end the loop
        game_over = True  

# If the user runs out of attempts and hasn't guessed the correct number

# Check if the game is still not over (i.e., the user didn't guess the number)
if not game_over:  

    # Inform the user they lost and reveal the correct number
    print("Game Over! You've used all", max_attempts, "attempts. The correct number was", random_number, ".")  
