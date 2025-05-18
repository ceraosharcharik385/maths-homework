def add_numbers(a: int, b: int) -> int:
    """
    Add two integers.
    
    Parameters:
    a (int): The first integer to be added.
    b (int): The second integer to be added.

    Returns:
    int: The sum of the two integers.
    """
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    """
    Subtract one number from another.

    Parameters:
    a (int): The first number from which another is subtracted.
    b (int): The second number to be subtracted from the first.

    Returns:
    int: The result of the subtraction.
    """
    return a - b

def multiply_numbers(a: int, b: int) -> int:
    """
    Multiply two numbers.

    Parameters:
    a (int): The first number to be multiplied.
    b (int): The second number to be multiplied by the first.

    Returns:
    int: The product of the two numbers.
    """
    return a * b

def divide_numbers(a: int, b: int) -> float:
    """
    Divide one number from another and returns the result as a floating-point number.

    Parameters:
    a (int): The numerator.
    b (int): The denominator or divisor.

    Returns:
    float: The quotient of the division.
    """
    return float(a / b)

def calculate_average(numbers: list[int]) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    numbers (list[int]): A list of integers to be averaged.

    Returns:
    float: The average of the provided numbers.
    """
    if not numbers:
        return 0.0
    else:
        return sum(numbers) / len(numbers)

# Example usage
print(add_numbers(5, 3))  # Output: 8
print(subtract_numbers(10, -2))  # Output: 8
print(multiply_numbers(4, 6))  # Output: 24
print(divide_numbers(9, 3))  # Output: 3.0
