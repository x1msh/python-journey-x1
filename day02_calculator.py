# day02_calculator.py
# X1's Python Journey - Day 2
# Date: 2026-07-07

# input() always returns a STRING, even if the user types a number
# We must convert it to an int or float before doing math

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert strings to floats (decimals)
num1_float = float(num1)
num2_float = float(num2)

result = num1_float + num2_float

print(f"The sum of {num1_float} and {num2_float} is {result}")

