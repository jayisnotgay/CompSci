n=eval(input("countdown= "))
while True:
    print(n,"...",sep=" ")
    n= n-1
    if n == -1:
        break
print("blast off!!")