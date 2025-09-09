"""1) Write a function calculate_circle_area(radius) that:
Takes the radius of a circle.
Returns the area of ​​a circle.
Use this function in a program that asks the user for a radius and prints out the area."""

import math


# Calculate the area of a circle given its radius
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

#request to user and output of the result
radius = float(input("Enter the radius of a circle: "))

print("Circle area: ", round(calculate_circle_area(radius),2))
