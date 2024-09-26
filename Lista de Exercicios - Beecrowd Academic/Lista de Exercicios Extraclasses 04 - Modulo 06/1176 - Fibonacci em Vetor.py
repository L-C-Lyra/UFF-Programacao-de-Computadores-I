import math

t = int(input())

for _ in range(t):
    n = int(input())

    fib = int((pow((1 + math.sqrt(5)) / 2, n) - pow((1 - math.sqrt(5)) / 2, n)) / math.sqrt(5))

    print(f'Fib({n}) = {fib}')
