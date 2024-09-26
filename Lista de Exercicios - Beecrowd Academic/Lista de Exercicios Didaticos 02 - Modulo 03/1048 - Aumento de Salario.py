def salary_adj_calc(adj_pct, salary):
    gain_adj = (adj_pct * salary) / 100
    return gain_adj


def main():
    salary = float(input())
    new_salary = 0.00

    if salary <= 400.00:
        gain_adj = salary_adj_calc(15, salary)
        new_salary = salary + gain_adj
        in_pct = 15
    elif salary <= 800.00:
        gain_adj = salary_adj_calc(12, salary)
        new_salary = salary + gain_adj
        in_pct = 12
    elif salary <= 1200.00:
        gain_adj = salary_adj_calc(10, salary)
        new_salary = salary + gain_adj
        in_pct = 10
    elif salary <= 2000.00:
        gain_adj = salary_adj_calc(7, salary)
        new_salary = salary + gain_adj
        in_pct = 7
    else:
        gain_adj = salary_adj_calc(4, salary)
        new_salary = salary + gain_adj
        in_pct = 4

    print(f'Novo salario: {new_salary:.2f}')
    print(f'Reajuste ganho: {gain_adj:.2f}')
    print(f'Em percentual: {in_pct} %')


if __name__ == '__main__':
    main()
