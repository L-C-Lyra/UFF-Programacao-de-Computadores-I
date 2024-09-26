option = 1
games_played = 0
v_int = 0
v_gre = 0
draw = 0

while option == 1:
    games_played += 1
    goals_int, goals_gre = map(int, input().split())
    if goals_int > goals_gre:
        v_int += 1
    elif goals_int < goals_gre:
        v_gre += 1
    else:
        draw += 1
    print(f'Novo grenal (1-sim 2-nao)')
    option = int(input())

print(f'{games_played} grenais')
print(f'Inter:{v_int}')
print(f'Gremio:{v_gre}')
print(f'Empates:{draw}')

if v_int > v_gre:
    print('Inter venceu mais')
elif v_int < v_gre:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
