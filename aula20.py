def soma(a, b):
    print(f'A = {a} e B = {b} ')
    s = a+b
    print(f'A soma vale A + B = {s}')
    print()
def contador(*n):
    print(f'Recebi os valores {n} e são ao todo {len(n)} números')
def dobra(lst):
    print(f'O dobro de {lst} é ',end='')
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)
def somavarios(*valores):
    s = 0
    for v in valores:
        s += v
    print(f'Somando os valores {valores} temos {s}')
def mensagem(msg):
    print('_'*30)
    print(msg)
    print('_'*30)


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=4, a=5)
contador(1,2)
contador(2,1,24,22)
valores = [6,3,9,1,0,2]
dobra(valores)
somavarios(2,1)
somavarios(2,1,3)
mensagem('SISTEMA DE ALUNOS')

