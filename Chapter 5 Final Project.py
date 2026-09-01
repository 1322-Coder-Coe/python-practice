"""
Chapter 5 – Official Project: Fantasy Game Inventory
This is the main practice project at the end of Chapter 5.
Project Description
You are creating a fantasy game inventory system using a dictionary.
The inventory will look like this:
inventory = {
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1,
    'arrow': 12
}
Part 1: Display Inventory
Write a function named display_inventory(inventory) that prints the inventory in this format:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

Requirements:
Print the word Inventory:
Loop through the dictionary and print each item and its quantity
At the end, print the total number of all items

Part 2: Add Items to Inventory
Write a second function named add_to_inventory(inventory, added_items).
This function should:
Take the current inventory (dictionary)
Take a list of newly looted items (example: ['gold coin', 'gold coin', 'ruby', 'dagger'])
Add those items to the inventory
Return the updated inventoryy
Example:
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
Expected output:
Inventory:
45 gold coin
1 rope
1 dagger
1 ruby
Total number of items: 48
"""
# Chapter 5 Official Project: Fantasy Game Inventory


def display_inventory(inventory):
  print("Inventory:")
  total_items = 0
  for item, count in inventory.items():
    print(f"{count} {item}")
    total_items += count
  print(f"Total number of items: {total_items}\n")


def add_to_inventory(inventory, added_items):
  for item in added_items:
    inventory[item] = inventory.get(item, 0) + 1
  return inventory


# 1. Initial inventory setup
inventory = {
    'gold coins': 200,
    'health potions': 5,
    'sword': 1,
    'bow': 1,
    'arrows': 99,
    'gems': 20,
}

# Display the starting inventory
print('--- Initial Inventory ---')
display_inventory(inventory)

# 2. Define newly looted items from an encounter
dragon_loot = ['gold coins', 'ruby', 'gold coins', 'health potions', 'shield']

# 3. Add the loot to the inventory dictionary
inventory = add_to_inventory(inventory, dragon_loot)

# 4. Display the final updated inventory
print('--- Updated Inventory After Loot ---')
display_inventory(inventory)

