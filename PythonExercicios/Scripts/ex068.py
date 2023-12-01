from random import randint
from time import sleep
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
result = ''
ganhos = 0
pc = 0
while True:
    pc = randint(1, 10)
    n =  int(input('Digite um valor: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if (pc + n) % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print('_' * 30)
    print(f'Você jogou {n} e o computador {pc}. Total de {pc + n} e deu {result}')
    print('_' * 30)
    if tipo == result[0]:
        ganhos += 1
        sleep(1)
        print('Você VENCEU!\nVamos jogar novamente ...')
        print('=-' * 30)
    else:
        break
print('Você PERDEU!')
sleep(1)
print('=-'*30)
sleep(1)
print(F'GAME OVER! Você venceu {ganhos} vezes')






