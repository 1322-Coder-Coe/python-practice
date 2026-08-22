"""
===============================================================================
Chapter 3: Functions
Automate the Boring Stuff with Python
===============================================================================
Topics covered in this chapter:
- Defining functions with def
- Parameters and arguments
- return statements
- Local vs global scope
- Default parameters
- Exception handling with try / except
- None return value

This file contains all practice exercises and solutions related to Chapter 3
from the practice files submitted during learning.
===============================================================================
"""

# -----------------------------------------------------------------------------
# Step 1 (from Book_chp_3 practice.py)
# Create a function called greet that prints two lines, then call it.
# -----------------------------------------------------------------------------
def greet():
    print("Hi there!")
    print("Welcome!")

greet()


# -----------------------------------------------------------------------------
# Step 2
# Create a function called say_hello that takes one parameter.
# -----------------------------------------------------------------------------
def say_hello(person):
    print("Hi, " + person + "!")

say_hello("James")
say_hello("Carl")


# -----------------------------------------------------------------------------
# Step 3
# Function with two parameters.
# -----------------------------------------------------------------------------
def describe(name, color):
    print(name + " likes the color " + color + ".")

describe("John", "Black")
describe("Wade", "Red")


# -----------------------------------------------------------------------------
# Step 4
# Function that returns a value (multiply).
# -----------------------------------------------------------------------------
def multiply(x, y):
    return x * y

result = multiply(3, 5)
print(result)


# -----------------------------------------------------------------------------
# Step 5
# Function that returns a value and is printed directly.
# -----------------------------------------------------------------------------
def subtract(a, b):
    return a - b

print(subtract(10, 3))


# -----------------------------------------------------------------------------
# Chapter 3 Practice Question 1 – Refactor tax calculation
# -----------------------------------------------------------------------------
def calculate_total(price, tax):
    tax = price * tax
    total = price + tax
    print("Total price: " + "$" + str(total))

calculate_total(50, 0.10)
calculate_total(120, 0.10)
calculate_total(80, 0.10)


# -----------------------------------------------------------------------------
# Refactor: print_user_tag
# -----------------------------------------------------------------------------
def print_user_tag(user):
    tag = "=== USER:" + user.upper() + " ==="
    print(tag)

print_user_tag("alice")
print_user_tag("bob")
print_user_tag("charlie")


# -----------------------------------------------------------------------------
# Function Execution Timing
# -----------------------------------------------------------------------------
print("Starting script...")

def show_message():
    print("Executing show_message function...")

print("Middle of script...")

# Function is called here
show_message()

print("Ending script...")


# -----------------------------------------------------------------------------
# Fix the missing statement – build_banner
# -----------------------------------------------------------------------------
def build_banner():
    print("==========================")
    print("   WELCOME TO THE GAME    ")
    print("==========================")

build_banner()


# -----------------------------------------------------------------------------
# calculate_area – call the function
# -----------------------------------------------------------------------------
def calculate_area():
    length = 5
    width = 4
    print("Area:", length * width)

calculate_area()


# -----------------------------------------------------------------------------
# Global vs Local Scope
# -----------------------------------------------------------------------------
character = "Knight"  # global scope

def cast_spell():
    spell_name = "Fireball"  # local scope
    print(character, "casts", spell_name)

cast_spell()

# Question: Which variable is in the global scope, and which variable is in the local scope?
# Answer: character is global, spell_name is local.


# -----------------------------------------------------------------------------
# square function with return
# -----------------------------------------------------------------------------
def square(number):
    return number * number

result = square(6)
print("The square is:", result)


# -----------------------------------------------------------------------------
# Default parameter example
# -----------------------------------------------------------------------------
def send_notification(message, sender="System"):
    print("[" + sender + "]: " + message)

# Line 1: Call to print "[System]: Server rebooting"
send_notification("Server rebooting", sender="System")

# Line 2: Call to print "[Admin]: Maintenance required"
send_notification("Maintenance required", sender="Admin")


# -----------------------------------------------------------------------------
# Functions return None by default
# -----------------------------------------------------------------------------
def log_event(event):
    print("LOGGED:", event)

status = log_event("User logged in")
print(status)  # This will print None


# -----------------------------------------------------------------------------
# global statement example
# -----------------------------------------------------------------------------
score = 100

def reset_score():
    global score
    score = score - score

reset_score()
print(score)  # Now prints 0


# -----------------------------------------------------------------------------
# check_data_type – print the type of None
# -----------------------------------------------------------------------------
def check_data_type():
    data = None
    print(type(data))

check_data_type()


# -----------------------------------------------------------------------------
# Exception handling – convert_to_number
# -----------------------------------------------------------------------------
def convert_to_number(text_val):
    try:
        val = int(text_val)
        print(val)
    except ValueError:
        print("Invalid number format!")

convert_to_number("42")      # Should convert successfully
convert_to_number("hello")   # Should trigger the exception


# -----------------------------------------------------------------------------
# Exception handling – get_average (handles empty list / ZeroDivisionError)
# -----------------------------------------------------------------------------
def get_average(numbers):
    try:
        total = sum(numbers)
        return total / len(numbers)
    except:
        return 0

print(get_average([10, 20, 30]))  # Should return 20.0
print(get_average([]))            # Should return 0 instead of crashing


# -----------------------------------------------------------------------------
# Challenge 5 from python_practice_ch1_to_ch4_set1.py
# Add Two Numbers (Function)
# -----------------------------------------------------------------------------
def add_numbers(a, b):
    result = a + b
    print(result)

add_numbers(7, 7)


# -----------------------------------------------------------------------------
# Collatz Sequence Project (Chapter 3 practice project)
# -----------------------------------------------------------------------------
def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = (3 * number) + 1
        print(result)
        return result

# Uncomment the two lines below to test the function alone:
# collatz(6)
# collatz(3)

# Full sequence loop
user_num = int(input("Let's start the Collatz Sequence! Provide me a number: "))

while user_num != 1:
    user_num = collatz(user_num)


print("\n--- End of Chapter 3 practice exercises ---")
