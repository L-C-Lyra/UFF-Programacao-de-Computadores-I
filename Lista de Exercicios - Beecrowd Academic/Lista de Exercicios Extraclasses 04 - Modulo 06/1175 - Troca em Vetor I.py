n = list()
i = 0
j = 19

for _ in range(20):
    x = int(input())
    n.append(x)

while i <= 10 <= j:
    n[i], n[j] = n[j], n[i]
    i += 1
    j -= 1

for i in range(len(n)):
    print(f'N[{i}] = {n[i]}')
