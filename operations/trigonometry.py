# operations/trigonometry.py
import math


def calculate_trigonometry(operation, numbers):
    if operation == 'sin':
        if len(numbers) == 1:
            return sine(numbers[0])
        else:
            print("Error: Sine operation takes exactly one number (in degrees).")
            return None
    elif operation == 'cos':
        if len(numbers) == 1:
            return cosine(numbers[0])
        else:
            print("Error: Cosine operation takes exactly one number (in degrees).")
            return None
    elif operation == 'tan':
        if len(numbers) == 1:
            return tangent(numbers[0])
        else:
            print("Error: Tangent operation takes exactly one number (in degrees).")
            return None
    elif operation == 'arcsin':
        if len(numbers) == 1:
            return arcsin(numbers[0])
        else:
            print("Error: Tangent operation takes exactly one number (in degrees).")
            return None
    elif operation == 'arccos':
        if len(numbers) == 1:
            return arccos(numbers[0])
        else:
            print("Error: Tangent operation takes exactly one number (in degrees).")
            return None
    elif operation == 'arctan':
        if len(numbers) == 1:
            return arctan(numbers[0])
        else:
            print("Error: Tangent operation takes exactly one number (in degrees).")
            return None
    else:
        print("Error: Invalid scientific operation.")
        return None


def arcsin(x):
    return math.degrees(math.asin(x))


def arccos(x):
    return math.degrees(math.acos(x))


def arctan(x):
    return math.degrees(math.atan(x))


def sine(degrees):
    return math.sin(math.radians(degrees))


def cosine(degrees):
    return math.cos(math.radians(degrees))


def tangent(degrees):
    return math.tan(math.radians(degrees))
