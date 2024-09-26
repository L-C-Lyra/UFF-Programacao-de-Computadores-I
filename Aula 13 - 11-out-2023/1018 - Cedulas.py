n = int(input())

banknotes = [100, 50, 20, 10, 5, 2, 1]

print(n)

for banknote in banknotes:
    counts_ballots = n // banknote
    n = n % banknote
    print(f'{counts_ballots} nota(s) de R$ {banknote},00')