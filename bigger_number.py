# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

first_number = float(input("First number: "))
second_number = float(input("Second number: "))

print(f"{first_number if first_number > second_number else second_number} is larger.")