def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers: A list of numbers.
        
    Returns:
        The sum of the numbers in the list.
    """
    if not numbers:
        return 0
    else:
        return sum(numbers)

# Example usage:
result = calculate_sum([1, 2, 3, 4])
print("The sum is:", result)
