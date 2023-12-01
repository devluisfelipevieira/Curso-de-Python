from random import randint
from time import sleep
print('_'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('_'*30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3,f' SORTEANDO {n} JOGOS','-='*3)
jogo = []
valor = 0
for v in range(1,n+1):
    for c in range(0,6):
        while True:
            valor = randint(0,60)
            if valor not in jogo:
                jogo.append(valor)
                break
    jogo.sort()
    print(f'Jogo {v}: {jogo}')
    jogo.clear()
    sleep(1)
print('{:-^30}'.format(' < BOA SORTE > '))
