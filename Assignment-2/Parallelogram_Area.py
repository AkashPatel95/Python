#Write a Python program to calculate the area of a parallelogram.
def parallelogram_area(base, height):
    area = base * height
    return area


base = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))

area = parallelogram_area(base, height)
print("The area of the parallelogram is: {:.2f}".format(area))
