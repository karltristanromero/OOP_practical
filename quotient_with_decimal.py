# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

try:
    print(f"Quotient: {first_number / second_number}")
except ZeroDivisionError:
    print("Can't divide by zero")