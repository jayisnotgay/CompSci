# User inputs plane's take off speed and acceleration
v=eval(input("Enter the plane's take off speed in m/s= "))
a=eval(input("Enter the plane's acceleration in m/s**2= "))

# Calculating the minimum runway
runway= v**2/(2*a)

#Output
print(f"The minimum runway length needed for this airplane is {runway} meters")