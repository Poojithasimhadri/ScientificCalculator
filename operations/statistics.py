# operations/scientific.py
import math


def square_root(number):
    return math.sqrt(number)





def mean(numbers):
    return sum(numbers) / len(numbers)


def variance(numbers):
    mean_value = mean(numbers)
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)


def standard_deviation(numbers):
    return math.sqrt(variance(numbers))
