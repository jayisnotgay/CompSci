import math

# User inputs the side length of a hexagon
side=eval(input("Enter the side length of the hexagon= "))
if side<0:
    side = eval(input("Please enter a positive number of the hexagon length= "))

# Calculates the hexagon area
area=(3*math.sqrt(3)*side**2)/2

# Output
print(f"The area of a hexagon with side length {side} is {area}")