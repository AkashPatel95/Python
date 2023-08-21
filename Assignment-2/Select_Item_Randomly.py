#Write a Python program to select an item randomly from a list.

import random

def random_item_from_list(input_list):
    return random.choice(input_list)

items_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random_item = random_item_from_list(items_list)

print("List of items:", items_list)
print("Randomly selected item:", random_item)
