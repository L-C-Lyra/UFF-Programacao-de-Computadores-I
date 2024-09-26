def pct_test_subj_calc(no_test_subj, tot_no):
    test_subj_pct = (no_test_subj * 100) / tot_no
    return test_subj_pct


def main():
    n = int(input())
    tot_no = 0
    no_rabbits = 0
    no_rats = 0
    no_frogs = 0

    for _ in range(n):
        test_case = list(input().split())
        quantia = int(test_case[0])
        tipo = test_case[1]

        if tipo == 'C':
            no_rabbits += quantia
        elif tipo == 'R':
            no_rats += quantia
        elif tipo == 'S':
            no_frogs += quantia

        tot_no += quantia

    print(f'Total: {tot_no} cobaias')
    print(f'Total de coelhos: {no_rabbits}')
    print(f'Total de ratos: {no_rats}')
    print(f'Total de sapos: {no_frogs}')
    print(f'Percentual de coelhos: {pct_test_subj_calc(no_rabbits, tot_no):.2f} %')
    print(f'Percentual de ratos: {pct_test_subj_calc(no_rats, tot_no):.2f} %')
    print(f'Percentual de sapos: {pct_test_subj_calc(no_frogs, tot_no):.2f} %')


if __name__ == '__main__':
    main()
