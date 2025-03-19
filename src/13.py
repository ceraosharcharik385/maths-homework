
import random

def get_random_maths_homework():
    # Generate a random number between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*", "/"])
    answer = calculate_answer(num1, num2, operation)
    return f"{num1} {operation} {num2} = {answer}"

def calculate_answer(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        return num1 / num2

# Test the function with a few examples
print(get_random_maths_homework())
print(get_random_maths_homework())
print(get_random_maths_homework())