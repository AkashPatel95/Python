#How can you pick a random item from a list or tuple?
import random

my_list = [1, 2, 3, 4, 5]
my_tuple = ('apple', 'banana', 'orange', 'grape', 'kiwi')

random_item_from_list = random.choice(my_list)
random_item_from_tuple = random.choice(my_tuple)

print("Random item from the list:", random_item_from_list)
print("Random item from the tuple:", random_item_from_tuple)
