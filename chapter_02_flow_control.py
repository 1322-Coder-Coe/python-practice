"""
===============================================================================
Chapter 2: Flow Control
Automate the Boring Stuff with Python
===============================================================================
Topics covered in this chapter:
- Boolean values and comparison operators
- if / elif / else statements
- while loops
- for loops and range()
- break and continue
- import random

This file contains all practice exercises and solutions related to Chapter 2
from the practice files submitted during learning.
===============================================================================
"""

# -----------------------------------------------------------------------------
# Challenge A (from Practice_2.py)
# Ask for age and print whether the user is an adult or a minor.
# -----------------------------------------------------------------------------
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# -----------------------------------------------------------------------------
# Challenge B (from Practice_2.py)
# Simple password check.
# -----------------------------------------------------------------------------
password = "python123"
entered_password = input("Enter Password: ")
if entered_password == password:
    print("Access Granted")
else:
    print("Access Denied")


# -----------------------------------------------------------------------------
# Challenge C (from Practice_2.py)
# Print numbers from 1 to 10 using a for loop.
# -----------------------------------------------------------------------------
for counting in range(1, 11):
    print(counting)


# -----------------------------------------------------------------------------
# Challenge D (from Practice_2.py)
# Keep asking for the password until the correct one is entered.
# -----------------------------------------------------------------------------
password = "secret"

entered_password = input("Enter Password: ")

while entered_password != password:
    print("Access Denied! Try again: ")
    entered_password = input("Enter Password: ")

print("Access Granted!")


# -----------------------------------------------------------------------------
# Challenge 2 (from retention_test_1.py)
# Ask for a number. If >= 100 print "That’s a big number!", else "That’s a small number."
# -----------------------------------------------------------------------------
number = int(input("Give me a number: "))
if number >= 100:
    print("That’s a big number!")
else:
    print("That's a small number.")


# -----------------------------------------------------------------------------
# Challenge 3 (from retention_test_1.py)
# Print all odd numbers from 1 to 15 using a for loop.
# -----------------------------------------------------------------------------
for odd in range(1, 16, 2):
    print(odd)


# -----------------------------------------------------------------------------
# Challenge 4 (from retention_test_1.py)
# Keep asking for a password until the user enters "python".
# -----------------------------------------------------------------------------
password = "python"
ent_pswrd = input("Enter Password: ")

while ent_pswrd != password:
    print("Sorry! Try again. ")
    ent_pswrd = input("Enter Password: ")
print("Correct Password!")


# -----------------------------------------------------------------------------
# Challenge 6 (from retention_test_1.py)
# Age category: child / teenager / adult
# -----------------------------------------------------------------------------
age = int(input("What is your age? "))

if age < 13:
    print("You are a child.")
elif age in range(13, 20):
    print("You are a teenager.")
else:
    print("You are an adult.")


# -----------------------------------------------------------------------------
# Challenge 1 (from Practice_2_Cont..py)
# Print numbers from 10 down to 1 (counting backwards).
# -----------------------------------------------------------------------------
for i in range(10, 0, -1):
    print(i)


# -----------------------------------------------------------------------------
# Challenge 2 (from Practice_2_Cont..py)
# Keep asking for a number between 1 and 5.
# If they enter 3, break and print a success message.
# -----------------------------------------------------------------------------
while True:
    number = int(input("Give me a number between 1 and 5: "))
    if number == 3:
        print("You found the special number!")
        break


# -----------------------------------------------------------------------------
# Challenge 2.1 (from Practice_2_Cont..py)
# Keep asking the user to type a word.
# If they type "quit", break and print “Goodbye!”.
# -----------------------------------------------------------------------------
while True:
    word = input("* Use 'quit' to stop * Type a word: ")
    if word == "quit":
        print("Goodbye!")
        break


# -----------------------------------------------------------------------------
# Challenge 3 (from Practice_2_Cont..py)
# Print numbers from 1 to 10, but skip the number 5 using continue.
# -----------------------------------------------------------------------------
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# -----------------------------------------------------------------------------
# Challenge 4 (from Practice_2_Cont..py)
# Import random and print 5 random numbers between 1 and 100.
# -----------------------------------------------------------------------------
import random
for _ in range(5):
    number = random.randint(1, 100)
    print(number)


# -----------------------------------------------------------------------------
# New Challenge 4 (from Practice_2_Cont..py)
# Generate 10 random numbers between 50 and 60 (inclusive).
# -----------------------------------------------------------------------------
import random

for _ in range(10):
    number = random.randint(50, 60)
    print(number)


# -----------------------------------------------------------------------------
# Challenge 2 from python_practice_ch1_to_ch4_set1.py
# Even or Odd
# -----------------------------------------------------------------------------
number = int(input("Provide a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# -----------------------------------------------------------------------------
# Challenge 3 from python_practice_ch1_to_ch4_set1.py
# Count to N
# -----------------------------------------------------------------------------
num = int(input("Provide a positive integer: "))
for x in range(1, num + 1):
    print(x)


# -----------------------------------------------------------------------------
# Challenge 4 from python_practice_ch1_to_ch4_set1.py
# Keep Asking Until Quit
# -----------------------------------------------------------------------------
ent_word = input("Type 'quit' to stop. Please enter something: ")
while ent_word != "quit":
    ent_word = input("Type 'quit' to stop. Please enter something: ")
    if ent_word == "quit":
        break
print("Goodbye!")


# -----------------------------------------------------------------------------
# Retention Test 1 (chp 1&2) – Full program
# Simple User Profile + Number Game
# -----------------------------------------------------------------------------
# Task 1: Get name
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Welcome, " + first_name + " " + last_name)

# Task 2: Age validation + category
while True:
    age = int(input("What is your age?"))
    if age >= 0:
        break
if age < 13:
    print("You are a Child.")
elif age < 18:
    print("You are a Teenager.")
elif age < 65:
    print("You are an Adult.")
else:
    print("You are a Senior.")

# Task 3: Number guessing game
import random

secret_num = random.randint(1, 10)
while True:
    guess = int(input("Guess the secret number between 1 & 10: "))
    if guess != secret_num:
        print("Wrong, try again.")
    else:
        print("Correct! Well done.")
        break

# Task 4: Final summary
full_name = first_name + " " + last_name
print("Thank you, " + full_name + ".")
print("Your full name consists of " + str(len(full_name)) + " letters.")
print(full_name + " " + full_name)


# -----------------------------------------------------------------------------
# Retention Test 2 (chp 1&2)
# Player info + difficulty + lucky number + counting
# -----------------------------------------------------------------------------
# Task 1
name = input("What is your first name?")
color = input("What is your favorite color? ")
print()
print("Welcome, " + name + " your favorite color is " + color + ".")
print()

# Task 2
while True:
    difficulty = int(input("Choose a difficulty level between 1-3: "))
    if difficulty in (1, 2, 3):
        break
    else:
        print("Invalid choice! Try again: ")
        print()
if difficulty == 1:
    print("Easy mode selected.")
elif difficulty == 2:
    print("Normal mode selected.")
elif difficulty == 3:
    print("Hard Mode Selected")

# Task 3
print()
import random

x = random.randint(1, 20)
print("Your lucky number is " + str(x) + ".")

# Task 4
for i in range(1, x + 1):
    if i == 7:
        continue
    print(i)

# Task 5
print()
print("Thank You for your input, " + name + "." + " There are " + str(len(name)) + " letters in your name." + " Your favorite  color is: " + (color + " ") * 3)


# -----------------------------------------------------------------------------
# Retention Test – Hard Mode (Hero Character Creator)
# -----------------------------------------------------------------------------
# 1: Create the Hero
hero_name = input("Enter your Hero's name:")
hero_weapon = input("Choose a weapon of choice:")
print()
print("A new Hero appears... " + hero_name + " the Brave, wielder of the " + hero_weapon + "!")

# 2: Choose Hero Class
print()
while True:
    user_class = input("Select a Hero Class (warrior, mage, or rogue):")
    if user_class.lower() in ("warrior", "mage", "rogue"):
        break
    else:
        print()
        print("ERROR: Classes can only be warrior, mage or rogue!")
        print()
if user_class.lower() == "warrior":
    print("You are a strong Warrior!")
elif user_class.lower() == "mage":
    print("You are a wise Mage!")
else:
    print("You are a stealthy Rogue!")

# 3: Generate Hero Stats
import random

strength = random.randint(5, 15)
health = random.randint(50, 100)

print("Strength: " + str(strength))
print("Health: " + str(health))

# 4: Mission Preparation Count
for x in range(1, strength + 1):
    if x == 10:
        continue
    print(x)

# 5: Final Mission Briefing
print()
print("Character Summary:")
print(hero_name + " the Brave's name is comprised of " + str(len(hero_name)) + " letters!")
print("Class: " + user_class)
print("Strength: " + str(strength) + " Health: " + str(health))
print("Weapon: " + hero_weapon + " " + hero_weapon)


print("\n--- End of Chapter 2 practice exercises ---")
