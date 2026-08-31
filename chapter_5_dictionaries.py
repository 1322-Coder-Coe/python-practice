"""
Practice 1
Create a dictionary called student with these keys and values:
'name': your name
'age': your age
'course': "Python"
Then print the value of 'name'.
"""
student = {'name': 'Evans Coe', 'age':'33', 'course':'Python'}
print(student)
"""
_____________________________________
Practice 2
Using the student dictionary, check if the key 'age' exists and print the result (True or False).
"""
print('age' in student)
"""
_____________________________________
Practice 3
Use .get() to try to get the key 'grade'. If it doesn’t exist, return "No grade yet".
"""
print(student.get('grade','No grade yet'))
"""
_____________________________________
Practice 4
Loop through the student dictionary and print each key and value in this format:
name → Evans Coe
"""
for key,value in student.items():
    print(key, "->",value)
"""
_____________________________________
Practice 5
Add a new key 'city' with the value "Accra" to the student dictionary, then print the whole dictionary.
"""
student ['city'] = 'Accra'
print(student)
"""
_____________________________________
Practice 6
Create this nested dictionary:
inventory = {
    'apple': 10,
    'banana': 25,
    'orange': 15
}
Then:
1.Print how many bananas there are
2.Add 5 more apples
3.Print the updated inventory
"""
inventory = {
    'apple': 10,
    'banana': 25,
    'orange': 15
}
#1: 
print("number of banana: " + str(inventory['banana']))
#2.
inventory['apple'] += 5
print("number of apples: " + str(inventory['apple']))
#3
print(inventory)
"""
_____________________________________
Practice 7
Create an empty dictionary called letter_count.
Loop through the string "programming" and count how many times each letter appears using setdefault().
Then print the dictionary."""

s = "programming"
letter_count = {}

for i in s:
    # 1. Check if letter 'i' is in the dictionary, if not, set its default value to 0, then add 1
    letter_count.setdefault(i, 0)
    letter_count[i] += 1

# 2. Print the final dictionary outside the loop
print(letter_count)

"""
_____________________________________
Practice 8
Create this nested dictionary:
users = {
    'alice': {'age': 25, 'city': 'Accra'},
    'bob': {'age': 30, 'city': 'Kumasi'},
    'carol': {'age': 22, 'city': 'Tamale'}
}
Then:
1.Print Bob’s age
2.Print Carol’s city
3.Add a new user 'dave' with age 28 and city "Cape Coast"
4.Print the whole users dictionary
"""
#0:
users = {
    'alice': {'age': 25, 'city': 'Accra'},
    'bob': {'age': 30, 'city': 'Kumasi'},
    'carol': {'age': 22, 'city': 'Tamale'}
}
#1:
print(users['bob']['age'])
#2:
print(users['carol']['city'])
users['dave'] = {'age': 28, 'city': 'Cape Coast'}
print(users)