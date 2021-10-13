myNames=[]
while True:
    name=input("Enter your name=")
    if not name:
        break
    if name[0].islower():
        print("Please enter capitalized name!")
        continue
    myNames.append(name)
print(myNames)
for name in myNames:
    print("Hi ", name, "!")
count = 0
for foo in myNames:
    count = count + 1
    print(count,".",foo)
