import math

def calculate_power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Parameters:
    base (float): The base number.
    exponent (int): The exponent.
    
    Returns:
    float: The result of base raised to the power of exponent.
    """
    return base ** exponent

# Example usage
base = 2.0
exponent = 3
result = calculate_power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result:.2f}")
