# --------------------------------------------------
# Author : Muhammad Hashim
# Student Number : 752451
# Revision Date : 15 June 2025
# Course Code : ICS3U
# Program : Expired Credit Cards Report
# Description : This program reads customer credit card data,
# identifies expired or soon-to-expire cards,
# validates them using the Luhn algorithm,
# sorts them by expiry date using merge sort,
# and displays a report to the console.
# --------------------------------------------------

"""
VARIABLE DICTIONARY:
first_names (list) = customer first names
last_names (list) = customer last names
card_types (list) = Visa or MasterCard card type
card_numbers (list) = 16-digit card numbers
expiry_months (list) = expiry months as integers
expiry_years (list) = expiry years as integers
expiry_dates (list) = converted dates in YYYYMM format for sorting
expired_indices (list) = list of indices of expired or soon-to-expire cards
sorted_indices (list) = indices sorted by expiry date
line (str) = one line from the input file
fields (list) = list of values from one line
"""

# Function to validate card number using Luhn Algorithm
def is_valid_luhn(number):
    total = 0  # holds the sum of processed digits
    number = number[::-1]  # reverse the card number string
    for i in range(len(number)):  # iterate through digits
        digit = int(number[i])  # convert char to int
        if i % 2 == 1:  # double every second digit
            digit = digit * 2
            if digit > 9:  # if two-digit number
                digit = digit - 9  # subtract 9
        total = total + digit  # add to running total
    return total % 10 == 0  # valid if total divisible by 10

# Function to perform merge sort on expiry dates using indices
def merge_sort(indices, expiry_dates):
    if len(indices) <= 1:  # base case: single element is sorted
        return indices
    mid = len(indices) // 2  # find middle index
    left = merge_sort(indices[:mid], expiry_dates)  # sort left half
    right = merge_sort(indices[mid:], expiry_dates)  # sort right half
    return merge(left, right, expiry_dates)  # merge two halves

# Merge function to combine two sorted lists
def merge(left, right, expiry_dates):
    result = []  # store merged result
    i = 0
    j = 0
    while i < len(left) and j < len(right):  # while both lists have elements
        if expiry_dates[left[i]] <= expiry_dates[right[j]]:  # compare expiry dates
            result.append(left[i])  # add from left if smaller or equal
            i = i + 1
        else:
            result.append(right[j])  # add from right if smaller
            j = j + 1
    result.extend(left[i:])  # append remaining from left
    result.extend(right[j:])  # append remaining from right
    return result

# Open the input file using the given path
file = open("/workspaces/ICS3UO/Data/data.dat", "r")  # open file for reading
lines = file.readlines()  # read all lines
file.close()  # close the file after reading

lines = lines[1:]  # skip the header line (first line)

# Initialize lists for each field
first_names = []
last_names = []
card_types = []
card_numbers = []
expiry_months = []
expiry_years = []
expiry_dates = []

# Process each line in the file after skipping header
for line in lines:
    line = line.strip()  # remove newline and whitespace
    fields = line.split(",")  # split by commas into fields
    first_names.append(fields[0])  # GivenName
    last_names.append(fields[1])  # Surname
    card_types.append(fields[2])  # CCType
    card_numbers.append(fields[3])  # CCNumber
    month = int(fields[4])  # Exp-Mo converted to int
    year = int(fields[5])  # Exp-Yr converted to int
    expiry_months.append(month)  # store month
    expiry_years.append(year)  # store year
    expiry_dates.append((year * 100) + month)  # convert to YYYYMM int for sorting

# Find cards that are expired or soon to expire (on or before June 2025)
expired_indices = []  # list to store indices of such cards
for i in range(len(expiry_dates)):
    if expiry_dates[i] <= 202506:  # check if card expiry is June 2025 or earlier
        if is_valid_luhn(card_numbers[i]):  # validate card number with Luhn
            expired_indices.append(i)  # add valid expired card index

# Sort the expired card indices by expiry date
sorted_indices = merge_sort(expired_indices, expiry_dates)

# Display the result to the console
for i in sorted_indices:
    name = first_names[i] + " " + last_names[i]  # combine first and last name
    card = card_types[i]  # card type (Visa or MasterCard)
    number = "#" + card_numbers[i]  # prepend # to card number
    # Format expiry date as YYYYMM with month zero-padded
    expiry = str(expiry_years[i]) + str(expiry_months[i]).zfill(2)
    # Determine status message based on expiry date
    if expiry_dates[i] < 202506:  # expiry before June 2025
        status = "EXPIRED"
    else:  # expiry exactly June 2025
        status = "RENEW IMMEDIATELY"
    # Print formatted output line to console
    print(name + ":    " + card + "    " + number + "  " + expiry + " " + status)
