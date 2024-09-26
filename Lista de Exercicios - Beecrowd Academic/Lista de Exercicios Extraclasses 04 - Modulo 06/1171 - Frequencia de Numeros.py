n = int(input())
x = list()

for _ in range(n):
    x_n = int(input())
    x.append(x_n)

for i in range(len(x) - 1):
    for j in range(len(x) - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]

for i in range(len(x)):
    aux = 0
    for j in range(i, len(x)):
        if x[i] == x[j]:
            aux += 1

    print(f'{x[i]} aparece {aux} vez(es)')