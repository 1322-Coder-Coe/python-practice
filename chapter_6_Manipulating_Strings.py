"""
Practice 1
Ask the user for their full name.
Then print:
The name in uppercase
The name in lowercase
How many characters it has (including spaces)
"""
name = input("What is your full name?: ")
print(name.upper())
print(name.lower())
print(len(name))

"""
Practice 2
Given this string:
message = "  Hello World  "
Do the following:
Remove the extra spaces from both ends
Replace "World" with "Python"
Print the final result
"""
message = "  Hello World  "
message = message.strip().replace("World", "Python")
print(message)
