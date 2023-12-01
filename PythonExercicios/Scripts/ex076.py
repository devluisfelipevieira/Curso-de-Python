print('_'*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('_'*30)
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.90,
         'Trasferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Caneta', 22.30,
         'Livro', 34.90)
n = 0
m = 1
while m < len(lista):
    print('{:.<30}R${:>7}'.format(lista[n], lista[m]))
    n += 2
    m += 2

 