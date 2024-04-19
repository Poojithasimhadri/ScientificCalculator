# operations/complex_numbers.py

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"


def add_complex(c1, c2):
    real_part = c1.real + c2.real
    imag_part = c1.imag + c2.imag
    return ComplexNumber(real_part, imag_part)


def subtract_complex(c1, c2):
    real_part = c1.real - c2.real
    imag_part = c1.imag - c2.imag
    return ComplexNumber(real_part, imag_part)


def multiply_complex(c1, c2):
    real_part = (c1.real * c2.real) - (c1.imag * c2.imag)
    imag_part = (c1.real * c2.imag) + (c1.imag * c2.real)
    return ComplexNumber(real_part, imag_part)


def divide_complex(c1, c2):
    divisor = c2.real ** 2 + c2.imag ** 2
    real_part = ((c1.real * c2.real) + (c1.imag * c2.imag)) / divisor
    imag_part = ((c1.imag * c2.real) - (c1.real * c2.imag)) / divisor
    return ComplexNumber(real_part, imag_part)
