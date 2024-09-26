n = int(input())

while n != 0:
    for aux_row in range(1, n + 1, 1):
        if aux_row == 1:
            print(f'{aux_row:3d}', end='')
            if n != 1:
                for aux_char in range(1, n - 1, 1):
                    print(f'{aux_char + 1:4d}', end='')
                print(f'{n:4d}')
            else:
                print()
        else:
            aux_inv_row = aux_row
            print(f'{aux_inv_row:3d}', end='')
            aux_inv_row -= 1
            for aux_inv_char in range(aux_inv_row, 0, -1):
                print(f'{aux_inv_char:4d}', end='')
                aux_inv_row -= 1
            aux_inv_row = aux_row
            aux_char = 2
            for _ in range(n - aux_inv_row):
                print(f'{aux_char:4d}', end='')
                aux_char += 1
            print()
    print()
    n = int(input())
