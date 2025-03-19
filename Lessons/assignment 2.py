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
random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
attempts = 0  # Initialize attempts count
max_attempts = 6  # Set the maximum number of attempts
game_over = False  # Boolean to control the loop

# Game Introduction
print("Welcome to the Number Guessing Game!")
print("I've picked a number between 1 and 100. Can you guess what it is?")
print("You have", max_attempts, "attempts to find the correct number. Good luck!")

# Game loop
while attempts < max_attempts and not game_over:
    attempts += 1  # Increment attempt count
    
    print("Attempt", attempts, ": Enter your guess:")
    user_input = int(input())  # Get user input
    
    if user_input > random_number:
        print("Too high! Try a lower number.")
    elif user_input < random_number:
        print("Too low! Try a higher number.")
    else:
        print("Congratulations! You guessed the number in", attempts, "tries! 🎉")
        game_over = True  # Set game_over to True to end the loop

# If user runs out of attempts
if not game_over:
    print("Game Over! You've used all", max_attempts, "attempts. The correct number was", random_number, ".")
