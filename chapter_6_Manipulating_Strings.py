"""
Practice 1
Ask the user for their full name.
Then print:
The name in uppercase
The name in lowercase
How many characters it has (including spaces)

name = input("What is your full name?: ")
print(name.upper())
print(name.lower())
print(len(name))


Practice 2
Given this string:
message = "  Hello World  "
Do the following:
Remove the extra spaces from both ends
Replace "World" with "Python"
Print the final result

message = "  Hello World  "
message = message.strip().replace("World", "Python")
print(message)

Practice 3
Create this list:
words = ["I", "love", "Python"]
Join the words into one sentence separated by spaces, so the result is:
I love Python
Print the final sentence.

words = ["I", "love", "Python"]
words= " ".join(words)
print(words)

Practice 4
Ask the user to enter a password.
Check if the password:
Is at least 8 characters long
Contains only letters and numbers (use .isalnum())
Print "Strong password" if both conditions are true, otherwise print "Weak password".
"""
password= input("Enter Password: ")

if len(password) >= 8 and password.isalnum():
    print("Strong password")
else:
    print("Weak password")