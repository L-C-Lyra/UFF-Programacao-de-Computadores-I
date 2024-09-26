n = int(input())

print(n)

hundred = n // 100
print(f'{hundred} nota(s) de R$ 100,00')

n -= hundred * 100
fifty = n // 50
print(f'{fifty} nota(s) de R$ 50,00')

n -= fifty * 50
twenty = n // 20
print(f'{twenty} nota(s) de R$ 20,00')

n -= twenty * 20
ten = n // 10
print(f'{ten} nota(s) de R$ 10,00')

n -= ten * 10
five = n // 5
print(f'{five} nota(s) de R$ 5,00')

n -= five * 5
two = n // 2
print(f'{two} nota(s) de R$ 2,00')

one = n - (two * 2)
print(f'{one} nota(s) de R$ 1,00')
