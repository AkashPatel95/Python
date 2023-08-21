#Write a Python program to read a random line from a file.
import random

def read_random_line(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        if lines:
            random_line = random.choice(lines)
            return random_line.strip()
        else:
            return "File is empty."

# Create and write to the file
filename = "random_lines.txt"

with open(filename, "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
    file.write("Line 4\n")
    file.write("Line 5\n")

# Read a random line from the file
random_line = read_random_line(filename)
print("Random line from the file:")
print(random_line)

