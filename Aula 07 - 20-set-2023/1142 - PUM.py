# Com Comando while:
# n = int(input())
# i = 0
# while i < n:
# 	print(...)
# 	i += 1

# Ler o Valor de n
n = int(input())
aux = 1

# Para cada uma das n Linhas faça
# for aux in range(1, n * 4, 4):
for i in range(n):
    # Imprimir a linha
    print(f'{aux} {aux + 1} {aux + 2} PUM')
    # Incrementar em 4 o Valor de aux
    aux += 4
