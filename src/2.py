import random

def get_random_python_code():
    code = """
x = {}
y = {}
print(x + y)
"""
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    return code.format(x, y)

get_random_python_code()