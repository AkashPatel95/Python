#Write a Python program to convert degree to radian.
def degrees_to_radians(degrees):
    radians = degrees * (3.14159 / 180)
    return radians


degrees = float(input("Enter degrees: "))
radians = degrees_to_radians(degrees)
print("{} degrees is equal to {} radians.".format(degrees, radians))
