"""
===============================================================================
Chapter 4: Lists
Automate the Boring Stuff with Python
===============================================================================
Topics covered in this chapter:
- Creating lists
- Indexing (positive and negative)
- Slicing
- Changing values in a list
- List concatenation and replication
- for loops with lists
- Methods: append(), insert(), remove(), sort(), etc.
- The in and not in operators
- Multiple assignment

This file contains all practice exercises and solutions related to Chapter 4
from the practice files submitted during learning.
===============================================================================
"""
"""
# -----------------------------------------------------------------------------
# Basic list example (from lists practice.py)
# Negative indexing
# -----------------------------------------------------------------------------
spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[-1])  # Prints 'elephant'


# -----------------------------------------------------------------------------
# Challenge 6 from python_practice_ch1_to_ch4_set1.py
# First and Last Item
# -----------------------------------------------------------------------------
animals_1 = ['dog', 'cat', 'rat', 'bat']
print(animals_1[0], animals_1[3])


# -----------------------------------------------------------------------------
# Challenge 7 from python_practice_ch1_to_ch4_set1.py
# Build a List
# Create an empty list and append numbers 1 through 5.
# Note: The original solution had a small bug (re-using the list name).
# Corrected version below:
# -----------------------------------------------------------------------------
empty_list = []

for i in range(1, 6):
    empty_list.append(i)

print(empty_list)


# -----------------------------------------------------------------------------
# Challenge 8 from python_practice_ch1_to_ch4_set1.py
# Print Each Item
# -----------------------------------------------------------------------------
colors = ['blue', 'green', 'black', 'purple']
for x in colors:
    print(x)


# -----------------------------------------------------------------------------
# Challenge 9 from python_practice_ch1_to_ch4_set1.py
# Check if Item Exists
# -----------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "date"]
test = input("What fruit would you like to look for? ")

if test in fruits:
    print("Found!")
else:
    print("Not found.")


# -----------------------------------------------------------------------------
# Challenge 10 from python_practice_ch1_to_ch4_set1.py
# Double the Numbers (Function + List)
# -----------------------------------------------------------------------------
def double_list(numbers):
    doubled = []
    for num in numbers:
        new_num = num * 2
        doubled.append(new_num)
    return doubled

my_list = [2, 4, 6, 8]
result = double_list(my_list)

print(result)
-------------------------------------
Gemini Practice: 
# Task 1: Print the 3rd item in the list using positive indexing.
# Task 2: Print the very last item using negative indexing.
# Task 3: Change "cat" to "lion" and print the updated list.

animals = ["dog", "cat", "bat", "elephant"]
#Task 1:
print(animals[2])
print(animals[-1])
animals[1] = "lion"
print(animals)
""" 
"""
_________________________________________________________________________
Missing Practice 1:

Create a list of numbers from 0 to 9:
Then do the following:
Print the first 4 numbers (using slicing)
Print the last 3 numbers (using slicing)
Print the numbers from index 2 to 6 (inclusive of 2, exclusive of 7)
Print the entire list using slicing

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0:4])
print(numbers[-3:])
print(numbers[2:7])
print(numbers[:])

_____________________________________

Next: Practice 2 of 7 – insert() and remove()

Create this list:
animals = ["dog", "cat", "elephant"]
Then do the following:
Use .insert() to add "rabbit" at index 1
Use .insert() to add "lion" at the beginning of the list
Use .remove() to delete "cat"
Print the final list
"""
animals = ["dog", "cat", "elephant"]

animals.insert(1,"rabbit")
print(animals)

animals.insert(0,"lion")
print(animals)

animals.remove("cat")
print(animals)