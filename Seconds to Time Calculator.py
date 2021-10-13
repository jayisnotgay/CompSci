print("Welcome to seconds to time calculator!")
seconds = int(input("Enter seconds= "))
hour = int(seconds // 3600)
minute = int((seconds - hour * 3600)//60)
second = int(seconds%60)
print(hour, minute, second)

print("Welcome to time to seconds calculator!")
hour = int(input("Enter hour= "))
minute = int(input("Enter minute= "))
second = int(input("Enter seconds= "))
seconds = hour * 3600 + minute * 60 + second
print(seconds)