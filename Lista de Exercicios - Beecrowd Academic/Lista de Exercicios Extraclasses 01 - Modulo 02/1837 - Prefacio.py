a, b = map(int, input().split())

q = a // b
r = a % b

if r < 0:
    r = r - b
    q = (a - r) // b

print(f'{q} {r}')
