""""
Chapter 4 – Official Practice Project 1: Comma Code

This is the first official practice project from the book.

Project Description:

Write a function named comma_code that takes a list as its argument and returns a string that joins the items together in the following format:

Items are separated by a comma and a space

The word "and" appears before the last item

Examples: 

spam = ['apples', 'bananas', 'tofu', 'cats']

print(comma_code(spam))
# Should print: apples, bananas, tofu, and cats

print(comma_code(['one']))
# Should print: one

print(comma_code([]))
# Should print: (empty string)

print(comma_code(['red', 'blue']))
# Should print: red, and blue

Requirements:
The function must return the string (do not just print it inside the function)
Handle lists with 0 items, 1 item, 2 items, and more than 2 items correctly
Do not use the join() method for this exercise (practice building the string manually)
"""
def comma_code(lists):
    if len(lists) == 0:
        return ""
        
    elif len(lists) == 1:
        return (lists[0])

print(comma_code([]))   
           
print(comma_code(["dog"]))   
    