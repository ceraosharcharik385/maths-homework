import random

def get_random_code():
    numbers = "0123456789"
    operators = "+-*/"
    variables = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(random.randint(10, 20)):
        code += random.choice(numbers)
        code += random.choice(operators)
        code += random.choice(variables) + "\n"
    return code
