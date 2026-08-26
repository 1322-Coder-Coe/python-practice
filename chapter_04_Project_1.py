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
    # Edge case 1: Empty list
    if len(lists) == 0:
        return ""
    
    # Edge case 2: Single-item list
    elif len(lists) == 1:
        return lists[0]
    
    # Edge case 3: Two-item list
    elif len(lists) == 2:
        return lists[0] + ", and " + lists[1]
    
    # General case: Three or more items
    else:
        results = ""
        # Loop through all items EXCEPT the very last one
        for i in range(len(lists) - 1):
            results += lists[i] + ", "
            
        # Add the word "and" and the final item at the end
        results += "and " + lists[-1]
        return results

# Test cases
print(comma_code(['apples', 'bananas', 'tofu', 'cats']))
# Output: apples, bananas, tofu, and cats

print(comma_code(['one']))
# Output: one

print(comma_code([]))
# Output: (empty string)

print(comma_code(['red', 'blue']))
# Output: red, and blue
