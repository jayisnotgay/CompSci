# User inputs
rows=eval(input("Rows: "))

# For loop to create the triangle (output)
for row in range(rows):
    for space in range(rows-row+1):
        print(" ",end=" ")
    for asterisk in range(row+1):
        print("*",end=" ")
    print("")