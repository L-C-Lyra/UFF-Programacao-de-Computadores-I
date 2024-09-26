sides = list(map(float, input().split()))

for i in range(len(sides) - 1):
    for j in range(len(sides) - 1):
        if sides[j] < sides[j + 1]:
            sides[j], sides[j + 1] = sides[j + 1], sides[j]

if sides[0] >= sides[1] + sides[2]:
    print('NAO FORMA TRIANGULO')
else:
    if pow(sides[0], 2) == pow(sides[1], 2) + pow(sides[2], 2):
        print('TRIANGULO RETANGULO')
    if pow(sides[0], 2) > pow(sides[1], 2) + pow(sides[2], 2):
        print('TRIANGULO OBTUSANGULO')
    if pow(sides[0], 2) < pow(sides[1], 2) + pow(sides[2], 2):
        print('TRIANGULO ACUTANGULO')
    if sides[0] == sides[1] and sides[1] == sides[2]:
        print('TRIANGULO EQUILATERO')
    elif (sides[0] == sides[1] or sides[1] == sides[2]) or sides[0] == sides[2]:
        print('TRIANGULO ISOSCELES')
