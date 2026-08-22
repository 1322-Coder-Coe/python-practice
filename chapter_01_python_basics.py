"""
===============================================================================
Chapter 1: Python Basics
Automate the Boring Stuff with Python
===============================================================================
Topics covered in this chapter:
- print() and input()
- Variables and assignment
- String concatenation and repetition
- len(), str(), int(), float()
- Basic arithmetic
- Comments

This file contains all practice exercises and solutions related to Chapter 1
from the practice files submitted during learning.
===============================================================================
"""

# -----------------------------------------------------------------------------
# Challenge A (from Practice1.py)
# Ask for name and age, then print a greeting.
# -----------------------------------------------------------------------------
print("What is your name?")
name = input()
print("How old are you?")
age = input()
print("Hello " + name + ", you are " + age + " years old.")


# -----------------------------------------------------------------------------
# Challenge B (from Practice1.py)
# Ask for a number and multiply it by 10.
# -----------------------------------------------------------------------------
print("Provide me a number.")
number = input()
print("Your number: " + number + " multiplied by 10 is: ")
print(int(number) * 10)


# -----------------------------------------------------------------------------
# Challenge C (from Practice1.py)
# Ask for first and last name, then thank the user.
# -----------------------------------------------------------------------------
print("What is your first name?")
first_name = input()

print("What is your last name?")
last_name = input()

print("Great! Thank you for your time " + first_name + " " + last_name + "!")


# -----------------------------------------------------------------------------
# Challenge D (from Practice1.py)
# Ask for a word and print how many letters it contains.
# -----------------------------------------------------------------------------
print("Provide me with a word and I will tell you how many letters it contains.")
word = input()
print("Your word " + word + " has " + str(len(word)) + " letters in it!")


# -----------------------------------------------------------------------------
# Challenge 1 (from retention_test_1.py)
# Ask for name and age, then print a formatted greeting.
# -----------------------------------------------------------------------------
name = input("What is your name? ")
age = input("How old are you? ")

print("Hello " + name + ", you are " + age + " years old.")


# -----------------------------------------------------------------------------
# Challenge 5 (from retention_test_1.py)
# Ask for a word. Print the word, its length, and the word repeated 3 times.
# -----------------------------------------------------------------------------
ent_word = input("Provide a word: ")
print("Your word is " + ent_word + ".")
print("It has " + str(len(ent_word)) + " letters in it.")
print((ent_word + " ") * 3)


# -----------------------------------------------------------------------------
# Challenge 1 from python_practice_ch1_to_ch4_set1.py
# Hello Name
# Ask the user for their name and print: Hello, <name>!
# -----------------------------------------------------------------------------
name = input("What is your name?")
greet = ("Hello, " + name + "!")
print(greet)


print("\n--- End of Chapter 1 practice exercises ---")
