# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

x = float(input("First number: "))
y = float(input("Second number: "))
print(f"{x if x > y else y} is larger.")