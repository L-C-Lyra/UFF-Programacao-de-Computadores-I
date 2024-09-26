pi = 3.14159
a, b, c = map(float, input().split())

area_triangle = (a * c)/ 2
area_circle = pi * c ** 2
area_trapeze = ((a + b) * c)/ 2
area_square = b ** 2
area_rectangle = a * b

print(f'TRIANGULO: {area_triangle:.3f}')
print(f'CIRCULO: {area_circle:.3f}')
print(f'TRAPEZIO: {area_trapeze:.3f}')
print(f'QUADRADO: {area_square:.3f}')
print(f'RETANGULO: {area_rectangle:.3f}')
