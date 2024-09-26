# Ler o valor x
x = int(input())

# Enquanto x != 0 faça
while x != 0:
    # Imprimir todos os valores de 1 até x (inclusive)
    # print(" ".join(map(str, range(1, x + 1))))
    for i in range(1, x):
        print(i, end=" ")
    print(x)
    # Ler o próximo valor x
    x = int(input())