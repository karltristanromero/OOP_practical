# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
 
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

remainder = x % y
print(f"The quotient of the numbers is {int(remainder)}.")