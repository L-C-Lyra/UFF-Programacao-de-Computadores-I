s, t, f = map(int, input().split())

p = s + t + f

if p > 24:
    p -= 24
elif p == 24:
    p = 0
elif p < 0:
    p += 24

print(p)
