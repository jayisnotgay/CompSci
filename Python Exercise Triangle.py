# User inputs triangle edges
edge1 = eval(input("Enter length of edge 1= "))
edge2 = eval(input("Enter length of edge 2= "))
edge3 = eval(input("Enter length of edge 3= "))

# Determining if the edges are valid and prints the output
if edge1 + edge2 > edge3 and edge2 + edge3 > edge1 and edge1 + edge3 > edge2:
    sum = edge1+edge2+edge3
    print(f'The perimeter is {sum}')
else:
    print("Input is invalid and the perimeter cannot be calculated.")