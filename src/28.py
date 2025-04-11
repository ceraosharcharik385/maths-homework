def add_numbers(x, y):
    """Add two numbers."""
    return x + y

def subtract_numbers(x, y):
    """Subtract one number from another."""
    return x - y

def multiply_numbers(x, y):
    """Multiply two numbers."""
    return x * y

def divide_numbers(x, y):
    """Divide one number by another."""
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")

def square_root_of_number(num):
    """Return the square root of a given number."""
    if num >= 0:
        return math.sqrt(num)
    else:
        raise ValueError("Number should be non-negative.")

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if len(numbers) == 0:
        raise ValueError("The list is empty.")
    
    total = sum(numbers)
    count = len(numbers)
    return total / count

# Example usage
if __name__ == "__main__":
    print(add_numbers(5, 3))   # Output: 8
    print(subtract_numbers(10, -2))   # Output: 8
    print(multiply_numbers(4, 5))   # Output: 20

    try:
        result = divide_numbers(4, 0)
        print(f"Result of division: {result}")
    except ValueError as e:
        print(e)

    print(square_root_of_number(9))
