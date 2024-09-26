import math


def fibonacci(n):
    fib = (pow((1 + math.sqrt(5)) / 2, n) - pow((1 - math.sqrt(5)) / 2, n)) / math.sqrt(5)
    print(f'{fib:.1f}')


def main():
    n = int(input())

    fibonacci(n)


if __name__ == "__main__":
    main()
