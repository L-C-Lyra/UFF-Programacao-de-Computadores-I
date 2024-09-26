a, b = map(float, input().split())

incr_percent = ((b - a) / a) * 100

print(f'{incr_percent:.2f}%')
