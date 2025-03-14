
import random

def get_random_python_code():
    lines = []
    for i in range(10):
        lines.append(f"{random.randint(1, 50)}")
    return "\n".join(lines)