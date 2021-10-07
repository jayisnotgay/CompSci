number_1 = eval(input("Enter the first number: "))
number_2 = eval(input("Enter the second number: "))
operator = eval(input("Select a number to choose an operator (1. Addition 2. Subtraction 3. Multiplication 4. Divide): "))

if operator==1:
    a = number_1 + number_2
    print (f"Result: {a}")
if operator==2:
    b = number_1 - number_2
    print (f"Result: {b} ")
if operator==3:
    c = number_1 * number_2
    print (f"Result: {c} ")
if operator==4:
    d = number_1 / number_2
    print (f"Result: {d} ")