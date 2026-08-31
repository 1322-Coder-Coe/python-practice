"""
Mini Project

Create a simple contact book using a dictionary.

Requirements:
1. Create a dictionary called contacts.
2. Add at least 3 people with this structure:
'name': {
    'phone': '...',
    'email': '...'
}
3. Print one person’s phone number.
4. Add a new contact.
5. Loop through all contacts and print them in this format:
Alice → Phone: 0244..., Email: alice@...
"""
#1&2: creating contact list
contacts = { 'Jacob': {'Phone': 6720013, 'Email': 'jacobvlack12@gmail.com'}, 'Felix': {'Phone': 6610089, 'Email': 'felix.lion77@gmail.com'}, 'Sandra': {'Phone': 6807733, 'Email': 'sandra.girly@gmail.com'}
}

#3: print one person's phone number
print(contacts['Jacob']['Phone'])

#4: adding a new contact
contacts['James'] = {'Phone': 6203476, 'Email': 'jamesbusline@gmail.com'}

#5: Loop through all contacts and print them nicely
for name, info in contacts.items():
    phone = info['Phone']
    email = info['Email']
    print(f"{name} → Phone: {phone}, Email: {email}")

