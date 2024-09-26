count_good_grades = 0
sum_grades = 0

while count_good_grades < 2:
    grade = float(input())
    if 0 <= grade <= 10:
        sum_grades += grade
        count_good_grades += 1
    else:
        print('nota invalida')

avg_grades = sum_grades / 2
print(f'media = {avg_grades:.2f}')
