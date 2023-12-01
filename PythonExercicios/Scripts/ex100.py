from random import randint
from time import sleep
numeros = list()
def sorteia(a):
    print(f'Sorteando os 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        n = randint(1, 10)
        print(n,end= ' ')
        sleep(0.5)
        numeros.append(n)
    sleep(0.5)
    print('PRONTO!')
    sleep(0.5)


def somaPar(lst):
    par = 0
    for p in lst:
        if p % 2 == 0:
            par += p
    print(f'Somando os valores pares de {numeros}, temos {par}')


sorteia(numeros)
somaPar(numeros)

