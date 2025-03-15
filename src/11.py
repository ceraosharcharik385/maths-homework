import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def get_random_integer(max_value):
    return random.randint(0, max_value)

def get_random_float(max_value):
    return random.uniform(0, max_value)

# Example usage:
# print(get_random_string(5))  # Output: "abcde"
# print(get_random_integer(10))  # Output: 7
# print(get_random_float(10.5))  # Output: 3.14