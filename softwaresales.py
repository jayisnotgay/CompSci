# User inputs packages purchased
quantity=eval(input("Enter the number of packages purchased= "))

# Determining the discount (in percent)
if 0<=quantity<=9:
    discount=0
elif 10<=quantity<=19:
    discount=10
elif 20<=quantity<=49:
    discount=20
elif 50<=quantity<=99:
    discount=30
elif 100<=quantity:
    discount=40

# Determining discount amount and total amount
price=99
discountamount=quantity*price*(discount/100)
total=(quantity*price)-discountamount

# Formatting currency
discountamountf="$ {:,.2f}".format(discountamount)
totalf="$ {:,.2f}".format(total)

# Output
print(f"Enter the number of packages purchased: {quantity}")
print(f"Discount amount @ {discount}% : {discountamountf}")
print(f"Total amount : {totalf}")