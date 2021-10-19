import math

# User input mass
mass=eval(input("Enter the mass of the kart (in kg)= "))

# User input force
force=eval(input("Enter the force to push the kart (in Newton)= "))

# Gravity variable
g=9.8

# Determining weight
weight=mass*g

# Determining sin theta
sintheta=force/weight

# Determining theta
angle=math.asin(sintheta)
angle2=math.degrees(angle)

# Output
print(f"the angle of the ramp is {angle2} degrees")