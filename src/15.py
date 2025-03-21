def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisor cannot be zero"

# Example usage
result1 = add_numbers(5, 3)
result2 = subtract_numbers(8, 4)
result3 = multiply_numbers(6, 7)
result4 = divide_numbers(9, 0)
