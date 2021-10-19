# User inputs point 1 coordinate
x1=eval(input("Enter the x cordinate of point 1= "))
y1=eval(input("Enter the y cordinate of point 1= "))

# User inputs point 2 coordinate
x2=eval(input("Enter the x cordinate of point 2= "))
y2=eval(input("Enter the y cordinate of point 2= "))

# Calculating the slope
slope=(y2-y1)/(x2-x1)

# Output
print(f"The slope for the line that connects two points ({x1},{y1}) and ({x2},{y2}) is {slope}")