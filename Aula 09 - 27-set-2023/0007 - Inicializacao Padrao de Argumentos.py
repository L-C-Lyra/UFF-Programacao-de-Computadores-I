# Inicialização Padrão de Argumentos Posicionais:
def procedure_name(arg1, arg2, arg3='Valor Padrão'):
    print(f'Procedure Call 1: {arg1}, {arg2}, {arg3}\n')


# Inicialização Padrão de Argumentos Posicionais E Nominais ( À Direita de * ):
def procedure_name2(arg1, arg2, *, arg3='Valor Padrão', arg4):
    print(f'Procedure Call 2: {arg1}, {arg2}, {arg3}, {arg4}\n')


procedure_name(10, 20)
procedure_name(10, 20, '30')
procedure_name2(10, 20, arg4=40)
procedure_name2(10, 20, arg3='30', arg4=40)
