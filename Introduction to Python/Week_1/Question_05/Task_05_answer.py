import math

# User input for the radius of the circle
radius = float(input("Enter radius of circle: "))

# Calculation of diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display the results with 'units'formatting
print(f'Diameter of circle = {diameter:.2f} units')
print(f'Circumference of circle = {circumference:.2f} units')
print(f'Area of circle = {area:.2f} sq. units')