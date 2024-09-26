n = int(input())

for _ in range(n):
    grade_1, grade_2, grade_3 = map(float, input().split())

    avg = ((grade_1 * 2) + (grade_2 * 3) + (grade_3 * 5)) / 10

    print(f'{avg:.1f}')
