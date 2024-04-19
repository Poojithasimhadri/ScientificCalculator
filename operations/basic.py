# operations/basic.py
def calculate_basic(operation, numbers):
    if operation == '+':
        return add(numbers)
    elif operation == '-':
        return subtract(numbers)
    elif operation == '*':
        return multiply(numbers)
    elif operation == '/':
        return divide(numbers)
    else:
        print("Error: Invalid basic operation.")
        return None


def add(numbers):
    return sum(numbers)


def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            print("Error: Cannot divide by zero")
            return None
    return result
