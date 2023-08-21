#How Do You Check The Presence Of A Key In A Dictionary?
my_dict = {"apple": 3, "banana": 5, "orange": 2}

key_to_check = "banana"

if key_to_check in my_dict:
    print(f"{key_to_check} is present in the dictionary.")
else:
    print(f"{key_to_check} is not present in the dictionary.")
