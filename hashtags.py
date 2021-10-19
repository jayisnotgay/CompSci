for i in range (7):
    for j in range (1, i+2):
        print(j, end="")
    print()

for i in range(7):
    print("#" * (7-i) )

for i in range(7, 0, -1):
    print('#' * i)

for i in range(7):
    print("#" * (1+i))

for i in range(7):
    print("#" * (7 - i), end="")
    for j in range (1, i+2):
        print(j, end="")
    print()

for i in range(7):
    print("#" * (7-i))
    for j in range (1, i+2):
        print(j, end="")

for i in range(7):
    print(" " * (7-i), end="")
    for j in range(1, i+2):
        print(j, end="")
    for j in range(i,0,-1):
        print(j, end="")
    print()






