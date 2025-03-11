import random

def get_random_number(n):
    return random.randint(1, n)

def main():
    number = get_random_number(10)
    print("Random Number:", number)

if __name__ == "__main__":
    main()
