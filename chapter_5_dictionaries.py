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
