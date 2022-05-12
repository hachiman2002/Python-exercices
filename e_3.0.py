"""
You are asked to make a program that allows you to enter any 2 numbers then
prints the sum and product of them.
"""
num_1 = float(input("Type the first number: "))
num_2 = float(input("Type the second number: "))
sum = num_1 + num_2
product = num_1 * num_2

print(f"Result sum = {sum:.1f}")
print(f"Result product = {product:.1f}")