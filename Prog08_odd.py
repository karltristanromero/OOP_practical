# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

print("Input 10 numbers")

odd = 0
for i in range(10):
    x = float(input(f"Enter number ({i+1}): "))
    if int(x) % 2 == 1:
        odd += 1

print(f"There are {odd} odd numbers.")