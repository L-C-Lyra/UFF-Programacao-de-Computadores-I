switch = True
switch_int = 1

while switch:
    grades_avg = 0

    grade_a = float(input())
    while grade_a < 0.0 or grade_a > 10.0:
        print('nota invalida')
        grade_a = float(input())

    grade_b = float(input())
    while grade_b < 0.0 or grade_b > 10.0:
        print('nota invalida')
        grade_b = float(input())

    grades_avg = (grade_a + grade_b) / 2.0
    print(f'media = {grades_avg:.2f}')

    print('novo calculo (1-sim 2-nao)')
    switch_int = int(input())
    while switch_int != 1 and switch_int != 2:
        print('novo calculo (1-sim 2-nao)')
        switch_int = int(input())
    if switch_int == 2:
        switch = False
