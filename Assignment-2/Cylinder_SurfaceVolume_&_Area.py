'''Write a Python program to calculate surface volume and area of a 
cylinder'''
def cylinder_surface_area(radius, height):
    lateral_surface_area = 2 * 3.14159 * radius * height
    base_surface_area = 2 * 3.14159 * radius**2
    total_surface_area = lateral_surface_area + base_surface_area
    return total_surface_area

def cylinder_volume(radius, height):
    volume = 3.14159 * radius**2 * height
    return volume


radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = cylinder_surface_area(radius, height)
volume = cylinder_volume(radius, height)

print("Surface area of the cylinder: {:.2f}".format(surface_area))
print("Volume of the cylinder: {:.2f}".format(volume))
