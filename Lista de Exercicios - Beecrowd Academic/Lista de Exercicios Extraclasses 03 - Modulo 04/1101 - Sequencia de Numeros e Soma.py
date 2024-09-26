m, n = map(int, input().split())

while m > 0 and n > 0:
    m_sum_n = 0

    if m > n:
        for i in range(n, m + 1, 1):
            m_sum_n += i
            print(f'{i}', end=' ')
        print(f'Sum={m_sum_n}')
    else:
        for i in range(m, n + 1, 1):
            m_sum_n += i
            print(f'{i}', end=' ')
        print(f'Sum={m_sum_n}')

    m, n = map(int, input().split())
