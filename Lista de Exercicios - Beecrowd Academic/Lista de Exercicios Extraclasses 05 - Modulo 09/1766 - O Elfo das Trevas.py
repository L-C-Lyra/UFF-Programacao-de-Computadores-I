def reindeer_ordered(elk):
    name, weight, age, height = elk
    return [-weight, age, height, name]


def main():
    t = int(input())
    test = 0

    for _ in range(t):
        test += 1
        n, m = map(int, input().split())
        reindeer = list()

        for _ in range(n):
            elk = input().split()
            elk[1], elk[2] = int(elk[1]), int(elk[2])
            elk[3] = float(elk[3])
            reindeer.append(elk)

        reindeer.sort(key=reindeer_ordered)

        print(f'CENARIO {{{test}}}')
        reindeer_pos = 1
        for i in range(m):
            print(f'{reindeer_pos} - {reindeer[i][0]}')
            reindeer_pos += 1


if __name__ == '__main__':
    main()
