# Exemplo de Procedimento COM RETURN


def sums(value1, value2):
    result = value1 + value2
    return result


# Exemplo de Procedimento SEM RETURN


def print_my_name(name):
    print('Hi, my name is', name)
    return None


x = float(input('Digite um valor para x: '))
y = float(input('Digite um valor para y: '))

s = sums(x, y)

print(f'A soma de {x} com {y} é {s}')

z = sums(x, 10)
w = sums(20, y)
h = sums(sums(x, y), sums(z, w))

print(f'A soma maluca é {h}')
