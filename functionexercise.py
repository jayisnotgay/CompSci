# 1

def convert_to_days():
    hours=eval(input("Enter hours: "))
    minutes=eval(input("Enter minutes: "))
    seconds=eval(input("Enter seconds: "))
    days=hours/24+minutes/(24*60)+seconds/(24*3600)
    return days

day=convert_to_days()
print(f"The number of days is: {day}")

#%%

# 2

def calc_weight_on_planet(wearth,gjupiter=23.1):
    g=9.8
    m=wearth/g
    w=m*gjupiter
    return w

weight = calc_weight_on_planet(120,9.8)
print(weight)

#%%

# 3

def num_atoms(amount,weight=196.97):
    avogadro=6.022*(10**23)
    number=amount/weight*avogadro
    return number

numofatoms=num_atoms(10)
print(numofatoms)

#%%

# 4

from fractions import Fraction

def calc_new_height():
    width=eval(input("Enter current width: "))
    height=eval(input("Enter current height: "))
    width2=eval(input("Enter desired width: "))
    ratio=Fraction(width,height)
    height2=width2/ratio
    return height2

h= calc_new_height()
print(h)

#%%

# 5

def convert_temp():
    fahrenheit=eval(input("Enter a temperature in Farenheit:"))
    return fahrenheit

def convert_celcius():
    celcius=5/9*(f-32)
    return celcius

def convert_kelvin():
    kelvin=c+273.15
    return kelvin

f=convert_temp()
c=convert_celcius()
k=convert_kelvin()
print(f"The temperature in fahrenheit is {f}")
print(f"The temperature in celcius is {c}")
print(f"The temperature in kelvin is {k}")