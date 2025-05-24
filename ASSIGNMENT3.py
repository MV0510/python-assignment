#Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(int(input("Enter the number:")))
print('The factorial of entered number is:',result)

#Task 2: Using the Math Module for Calculations

num = int(input("Enter a number:"))
from math import *
print("Square root:",sqrt(num))
print('Logarithm:',log(num,e))
print("Sine:",sin(num))
