import math


def quantity_prime_nums(n):
    p = n / math.log(n)
    m = 1.25506 * (n / math.log(n))
    print(f'{p:.1f} {m:.1f}')


def main():
    n = int(input())

    quantity_prime_nums(n)


if __name__ == "__main__":
    main()
