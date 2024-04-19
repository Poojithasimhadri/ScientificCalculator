# operations/exponential.py
import math


def calculate_exponential(operation, numbers):
    if operation == 'sqrt':
        if len(numbers) == 1:
            return square_root(numbers[0])
        else:
            print("Error: Square root operation takes exactly one number.")
            return None
    elif operation == 'exp':
        if len(numbers) == 1:
            return exp(numbers[0])
        else:
            print("Error: exp operation takes exactly one number (in degrees).")
            return None


def exp(x):
    return math.exp(x)


def square_root(number):
    return math.sqrt(number)
