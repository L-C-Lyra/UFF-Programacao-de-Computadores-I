n = int(input())
t = list(map(int, input().split()))
tormentor = float('inf')
t_tormentor = None

for i in range(n):
    if t[i] < tormentor:
        tormentor = t[i]
        t_tormentor = i + 1

print(t_tormentor)
