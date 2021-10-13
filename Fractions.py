import math

# Inputting numerator and denominator
numerator = int(input("Enter numerator= "))
while numerator <= 0:
    numerator = int(input("Please enter numerator greater than 0= "))
denominator = int(input("Enter denominator= "))
while denominator <= 0:
    numerator = int(input("Please enter denominator greater than 0= "))



gcd = math.gcd(numerator,denominator)
wholenumber = numerator//denominator
leftover = numerator%denominator

# Determining if the fraction is an improper fraction or a proper fraction
if numerator > denominator:
    print(f"{numerator}/{denominator} is an improper fraction.")
    # Determining if the improper fraction could be reduced or not, and if it could be a mixed fraction or a whole number
    if gcd !=1 and leftover != 0:
        print(f"This improper fraction is reduced to: {numerator//gcd}/{denominator//gcd}")
        print(f"The mixed fraction is {wholenumber} {leftover//gcd}/{denominator//gcd}")
    elif gcd !=1 and leftover == 0:
        print(f"The whole number is {wholenumber}")
    elif gcd ==1 and leftover != 0:
        print(f"This improper fraction cannot be reduced any further.")
        print(f"The mixed fraction is {wholenumber} {leftover//gcd}/{denominator//gcd}")
    elif gcd ==1 and leftover ==0:
        print(f"This improper fraction cannot be reduced any further.")
        print(f"The whole number is {wholenumber}")
if numerator < denominator:
    print(f"{numerator}/{denominator} is a proper fraction.")
    # Determining if the proper fraction could be reduced or not.
    if gcd != 1:
        print(f"This proper fraction is reduced to: {numerator//gcd}/{denominator//gcd}")
    elif gcd == 1:
        print(f"This proper fraction cannot be reduced any further.")
if numerator == denominator:
    print(f"The whole number is {wholenumber}")




