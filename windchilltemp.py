import math
# User inputs outside temperature
t = eval(input("Enter a temperature between -58 and 41 degrees Fahrenheit= "))
while True:
    if -58 <= t <= 41:
        break
    else:
        t = eval(input("Please re-enter a temperature between -58 and 41 degrees Fahrenheit= "))

# User inputs wind speed
v = eval(input("Enter wind speed greater than 2 mph= "))
while True:
    if v>2:
        break
    else:
        v = eval(input("Please re-enter wind speed greater than 2 mph= "))

# Calculating the wind chill temperature
twc=35.74 + 0.6215 * t - 35.75 * (v**0.16) + 0.4275 * (v**0.16) * t

# Formatting the result
twcf = "{:.3f}".format(twc)

# Output
print(f"The wind chill index is {twcf}")