import math

def calculate_squares(a, b):
    """
    Calculate the squares of two numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The sum of the squares of a and b.
    """
    return math.pow(a, 2) + math.pow(b, 2)

# Example usage
result = calculate_squares(3, 4)
print(result)
