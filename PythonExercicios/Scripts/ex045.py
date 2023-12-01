from random import randint
itens = ('\033[31mPEDRA\033[m','\033[32mPAPEL\033[m','\033[33mTESOURA\033[m')
pc = randint(0,2)
print('''Escolha entre:
\033[31m [0]PEDRA\033[m
\033[32m [1]PAPEL\033[m
\033[33m [2]TESOURA\033[m''')
jogador=int(input('Qual sua escolha? '))
print('-='*12)
print('Jogador jogou: {}'.format(itens[jogador]))
print('Computador jogou: {}'.format(itens[pc]))
print('-='*12)
if pc == 0:#pc jogou pedra
     if jogador == 0:
         print('Empate')
     elif jogador == 1:
         print('Jogador ganhou')
     elif jogador == 2:
         print('Jogador perdeu')
     else:
         print('JOGADA INVALIDA')
elif pc == 1:#pc jogou papel
    if jogador == 0:
        print('Jogador perdeu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador ganhou')
    else:
        print('JOGADA INVALIDA')
elif pc == 2:#pc jogou tesoura
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Jogador perdeu')
    elif jogador == 2:
        print('Empate')
    else:
        print('JOGADA INVALIDA')


