def fatorial(numero,show=False):
    """
    → Calcula o fatorial de um número;
    :param numero: O número a ser calculado;
    :param show: (opcional) Mostrar ou não a conta;
    :return: O valor do Fatorial de um número n.
    """
    print('_'*30)
    if show == False:
        f = 1
        for c in range(numero,0,-1):
            f *= c
        return f
    else:
        f = 1
        for c in range(numero, 0, -1):
            f *= c
            print(c, end=' ')
            if c > 1:
                print('X',end=' ')
        print('=',end=' ')
        return f


help(fatorial)
print(fatorial(5))
print(fatorial(5,True))