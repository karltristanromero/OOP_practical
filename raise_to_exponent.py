# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

result = first_number ** second_number
print(f"{first_number} raised to {second_number} is {result}")