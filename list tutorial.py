mynames = [0,1,2,3,4,5,6,7,8,9,"Hello"]
print(mynames)

# List slicing in Python

# includes element at index 2, 3, 4
# excludes element at index 5
print(mynames[2:5])

# elements beginning to 4th
print(mynames[:-5])

# elements 6th to end
print(mynames[5:])

# elements beginning to end
print(mynames[:])

# Correcting mistake values in a list
odd = [2, 4, 6, 8, 10, 12, 14, 16]

# change the 1st item
# odd[0] = 1

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)
