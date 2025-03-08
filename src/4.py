
import random
def get_random_code():
    """Return a randomly generated Python code snippet."""
    return ''.join(chr(random.randint(97, 122)) for _ in range(5))