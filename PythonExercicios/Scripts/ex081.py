lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    while True:
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
        if continuar[0] == 'S' or continuar[0] == 'N':
            break
    if continuar[0] == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 NÃO faz parte da lista')

