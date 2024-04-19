# main.py
import operations.basic as basic
import operations.exponential as exponential
import operations.trigonometry as trigonometry
import operations.complex_numbers as complex_numbers
import operations.statistics as statistics


def get_numbers():
    numbers = []
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num == "done":
            break

        num = float(num)
        numbers.append(num)

    return numbers


def parse_complex_number():
    while True:
        try:
            real = float(input("Enter the real part of the complex number: "))
            imag = float(input("Enter the imaginary part of the complex number: "))
            return complex_numbers.ComplexNumber(real, imag)
        except ValueError:
            print("Invalid input. Please enter valid real and imaginary parts.")


def calculate(operation, numbers):
    if operation in ['+', '-', '*', '/']:
        return basic.calculate_basic(operation, numbers)
    elif operation in ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan']:
        return trigonometry.calculate_trigonometry(operation, numbers)
    elif operation in ['exp', 'sqrt']:
        if len(numbers) == 1:
            return exponential.calculate_exponential(operation, numbers)
        else:
            print("Error: Exponential operation takes exactly one number.")
            return None
    elif operation == 'mean':
        if len(numbers) > 0:
            return statistics.mean(numbers)
        else:
            print("Error: Mean operation requires at least one number.")
            return None
    elif operation == 'variance':
        if len(numbers) > 0:
            return statistics.variance(numbers)
        else:
            print("Error: Variance operation requires at least one number.")
            return None
    elif operation == 'std_deviation':
        if len(numbers) > 0:
            return statistics.standard_deviation(numbers)
        else:
            print("Error: Standard Deviation operation requires at least one number.")
            return None
    elif operation == 'add_complex':
        if len(numbers) == 2:
            return complex_numbers.add_complex(numbers[0], numbers[1])
        else:
            print("Error: Complex addition operation requires exactly two complex numbers.")
            return None
    elif operation == 'subtract_complex':
        if len(numbers) == 2:
            return complex_numbers.subtract_complex(numbers[0], numbers[1])
        else:
            print("Error: Complex subtraction operation requires exactly two complex numbers.")
            return None
    elif operation == 'multiply_complex':
        if len(numbers) == 2:
            return complex_numbers.multiply_complex(numbers[0], numbers[1])
        else:
            print("Error: Complex multiplication operation requires exactly two complex numbers.")
            return None
    elif operation == 'divide_complex':
        if len(numbers) == 2:
            return complex_numbers.divide_complex(numbers[0], numbers[1])
        else:
            print("Error: Complex division operation requires exactly two complex numbers.")
            return None
    else:
        print("Error: Invalid operation.")
        return None


def main():
    while True:
        print("\nScientific Calculator")
        print("Basic operations: +, -, *, /")
        print("Scientific operations: sqrt, sin, cos, tan, arcsin, arccos, arctan, exp")
        print("Statistics operations: mean, variance, std_deviation")
        print("Complex number operations: add_complex, subtract_complex, multiply_complex, divide_complex")
        operation = input("Enter an operation (or 'quit' to exit): ")

        if operation.lower() == 'quit':
            break

        if operation in ['add_complex', 'subtract_complex', 'multiply_complex', 'divide_complex']:
            numbers = [parse_complex_number() for _ in range(2)]
        else:
            numbers = get_numbers()

        if len(numbers) == 0:
            print("Error: Please enter valid numbers.")
            continue

        result = calculate(operation, numbers)
        if result is not None:
            print("Result:", result)


if __name__ == "__main__":
    main()
