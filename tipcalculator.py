# User inputs subtotal and tip (in %)
subtotal=eval(input("Enter the subtotal= "))
tippercent=eval(input("Enter tip amount(as a %)= "))

# Calculating tip & total
tip=subtotal*(tippercent/100)
total=subtotal+tippercent

# Currency formatting
subf="$ {:,.2f}".format(subtotal)
tipf="$ {:,.2f}".format(tip)
totalf="$ {:,.2f}".format(total)

# Output
print(f"Subtotal: {subf}")
print(f"Tip: {tipf}")
print(f"Total: {totalf}")