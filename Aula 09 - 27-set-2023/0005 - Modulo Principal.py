from minha_primeira_funcao import sums

x = float(input('Digite um valor para x: '))
y = float(input('Digite um valor para y: '))

s = sums(x, y)

print(f'A soma de {x} com {y} é {s}')

z = sums(x, 10)
w = sums(20, y)
h = sums(sums(x, y), sums(z, w))

print(f'A soma maluca é {h}')
