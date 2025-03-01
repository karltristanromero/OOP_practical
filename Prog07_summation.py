# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

total_sum = 0

for i in range(10):
     x = float(input(f"Please input 10 numbers (Current number: {i+1}): "))
     total_sum += x

print(total_sum)