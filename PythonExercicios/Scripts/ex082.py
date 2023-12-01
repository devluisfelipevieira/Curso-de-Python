lista = []
par = []
impar = []
while True:
    valor = lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Digite "N" para parar: '))
    if continuar in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
