from math import sqrt

# Ler os Valores de a, b e c
# Para Humano: text = input('Digite os valores para A, B e C ( Na mesma Linha. ): ')
# Para Robô:
text = input()
numbers = text.split()
a = float(numbers[0])
b = float(numbers[1])
c = float(numbers[2])

# Calcular delta = b ** 2 - 4 * a * c
discriminant = b ** 2 - 4 * a * c

# Se é possível calcular as raízes então
if discriminant >= 0.0 and a != 0.0:
    # Calcular r1 = (-b + sqrt(delta)) / (2 * a)
    # Calcular r2 = (-b - sqrt(delta)) / (2 * a)
    r1 = ((-b) + sqrt(discriminant)) / (2 * a)
    r2 = ((-b) - sqrt(discriminant)) / (2 * a)
    # Mostrar as raízes
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
# Caso contrário, se não é possível calcular as raízes
else:
    # Mostrar que não é possível
    print('Impossivel calcular')
