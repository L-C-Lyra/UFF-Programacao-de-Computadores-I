grade_1, grade_2, grade_3, grade_4 = map(float, input().split())

avg = ((grade_1 * 2.0) + (grade_2 * 3.0) + (grade_3 * 4.0) + (grade_4 * 1.0)) / 10

print(f'Media: {avg:.1f}')

if avg < 5.0:
    print('Aluno reprovado.')
elif avg <= 6.9:
    print('Aluno em exame.')
    grade_ex = float(input())
    print(f'Nota do exame: {grade_ex:.1f}')
    avg_exam = (avg + grade_ex) / 2
    print('Aluno reprovado.' if avg_exam < 5.0 else 'Aluno aprovado.')
    print(f'Media final: {avg_exam:.1f}')
else:
    print('Aluno aprovado.')
