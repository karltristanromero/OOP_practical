# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point


x = float(input("First number: "))
y = float(input("Second number: "))

try:
    print(f"Quotient: {x / y}")
except ZeroDivisionError:
    print("Can't divide by zero")