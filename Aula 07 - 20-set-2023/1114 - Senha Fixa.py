# Ler senha
password = int(input())

# Enquanto senha for incorreta (senha != 2002) faça
while password != 2002:
    # Informar que a senha está incorreta
    print('Senha Invalida')
    # Ler senha
    password = int(input())
# Informar que a senha está correta
print('Acesso Permitido')
