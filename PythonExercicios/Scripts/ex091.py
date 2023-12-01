from random import randint
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
print('Valores sorteados:')
for k,v in jogo.items():
    print(f'    O {k} tirou {v}')
rank = []
rank = sorted(jogo.items(), key = itemgetter(1), reverse= True)
print('Ranking dos jogadores:')
for r,j in enumerate(rank):
    print(f'    {r+1}° lugar: {j[0]} com {j[1]} ')
