pair_no = 0
unpair_no = 0
positive_no = 0
negative_no = 0

for _ in range(5):
    no = int(input())

    if no % 2 == 0:
        pair_no += 1
    else:
        unpair_no += 1

    if no > 0:
        positive_no += 1
    elif no < 0:
        negative_no += 1

print(f'{pair_no} valor(es) par(es)')
print(f'{unpair_no} valor(es) impar(es)')
print(f'{positive_no} valor(es) positivo(s)')
print(f'{negative_no} valor(es) negativo(s)')
