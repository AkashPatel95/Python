#How can you pick a random item from a range?
import random

my_range = range(1, 11)  # Range from 1 to 10

random_item_from_range = random.choice(list(my_range))

print("Random item from the range:", random_item_from_range)
