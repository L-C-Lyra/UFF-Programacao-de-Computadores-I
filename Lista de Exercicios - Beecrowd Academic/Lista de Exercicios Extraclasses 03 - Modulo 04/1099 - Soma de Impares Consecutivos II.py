n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    sum_umpairs = 0

    start = min(x, y)
    end = max(x, y)

    for i in range(start + 1, end):
        if i % 2 != 0:
            sum_umpairs += i

    print(sum_umpairs)
