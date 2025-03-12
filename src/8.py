def get_random_number(n):
    import random
    numbers = []
    for i in range(n):
        number = random.randint(0, n)
        if number not in numbers:
            numbers.append(number)
    return numbers

print(get_random_number(5))
