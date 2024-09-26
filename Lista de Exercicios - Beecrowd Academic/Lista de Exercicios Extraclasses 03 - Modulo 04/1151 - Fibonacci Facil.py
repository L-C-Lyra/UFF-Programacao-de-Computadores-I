fib_a = 0
fib_b = 1

n = int(input())

if n == 0:
    print(fib_a)
elif n == 1:
    print(fib_a, fib_b, end=' ')
else:
    print(fib_a, fib_b, end=' ')
    for f in range(2, n):
        fib_c = fib_a + fib_b
        if f != n - 1:
            print(fib_c, end=' ')
        else:
            print(fib_c)
        fib_a = fib_b
        fib_b = fib_c
