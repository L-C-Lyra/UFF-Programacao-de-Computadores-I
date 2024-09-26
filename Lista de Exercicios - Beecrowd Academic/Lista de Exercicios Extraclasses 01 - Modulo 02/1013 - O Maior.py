text = input()
numbers = text.split()
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

maior_ab = int((a + b + abs(a - b)) / 2)

maior_mc = int((maior_ab + c + abs(maior_ab - c)) / 2)

print(f'{maior_mc:d} eh o maior')
