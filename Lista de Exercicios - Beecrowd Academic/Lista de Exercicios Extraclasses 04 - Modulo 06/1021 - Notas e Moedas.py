n = int(float(input()) * 100)

banknotes_f = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
coins_f = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
banknotes = [10000, 5000, 2000, 1000, 500, 200]
coins = [100, 50, 25, 10, 5, 1]

counts_ballots = list()
counts_coins = list()


for banknote in banknotes:
    count_ballot = n // banknote
    n = n % banknote
    counts_ballots.append(count_ballot)

for coin in coins:
    count_coin = n // coin
    n = n % coin
    counts_coins.append(count_coin)

print('NOTAS:')
for i in range(len(banknotes_f)):
    print(f'{counts_ballots[i]} nota(s) de R$ {banknotes_f[i]:.2f}')

print('MOEDAS:')
for j in range(len(coins_f)):
    print(f'{counts_coins[j]} moeda(s) de R$ {coins_f[j]:.2f}')
