def avg_status(avg):
    if avg < 4.0:
        return 'Reprovado'
    elif avg < 6.0:
        return 'Verificação Suplementar'
    else:
        return 'Aprovado'


def main():
    average = float(input('Informe a média do(a) aluno(a): '))

    average_status = avg_status(average)
    print(f'O status do(a) aluno(a) é: {average_status}.')


if __name__ == '__main__':
    main()
