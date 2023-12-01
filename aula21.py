def somar(a=0, b=0, c=0):
    """
    → Faz a soma de três valores e mostra a soma deles na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    Função criada por Luis Felipe ♪
    """
    s =  a + b + c
    return s


help(somar)
print(f'As somas valem : {somar(1,2,4)}, {somar(4,77,22)}, {somar()}')
r1 = somar(2,5)
r2 = somar(5,5)
print(f'As somas deram:\n{r1}\n{r2}')


def funcao():
    global n1  # Faz com que os metodos usados na variavel dentro da função também ocorram fora da função
    n1 = 4
    print(f'Dentro da função N1 vale {n1}')


n1 = 2
funcao()
print(f'Fora da função N1 vale {n1}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('Não é par')

