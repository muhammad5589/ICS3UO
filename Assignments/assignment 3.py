"""
   Author : Muhammad Hashim
   Student Number : 752451
   Revision Date : 23 April 2025
   Course Code : ICS3U
   Program : Palindrome Detector
   Description : This program checks a list of words and identifies which ones are palindromes.
   VARIABLE DICTIONARY :
     entries (list) = A list containing 10 words to check
     entry (string) = The current word being processed from the list
     position (int) = The index of the current character being compared
     match_counter (int) = Keeps track of how many characters have matched so far
     split_point (int) = The halfway point of the word used to limit the loop
     left (char) = Character from the start of the word
     right (char) = Character from the end of the word
"""
# Program introduction
print("Palindrome Detector: Let's check some words!")

# List of words to be checked
entries = ["deified", "mirror", "stats", "window", "civic", "orange", "rotator", "phone", "refer", "screen"]

# Loop through each entry
for entry in entries:
    position = 0
    match_counter = 0
    split_point = len(entry) // 2

    # Compare characters from both ends toward the center
    while position < split_point:
        left = entry[position]
        right = entry[len(entry) - 1 - position]

        if left == right:
            match_counter += 1
            position += 1
        else:
            print(entry + " is NOT a palindrome")
            position = split_point  # Exit the loop safely without break

        if match_counter == split_point:
            print(entry + " is a palindrome")

# Program ending
print("All words checked. Goodbye!")
