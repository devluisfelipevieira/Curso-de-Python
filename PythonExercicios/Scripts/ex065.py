continuar = ''
cont = media = maior = menor = 0
while continuar != 'N':
    n = float(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    cont += 1
    media += n
    if cont == 1:
        maior =  menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('Você digitou {} números e a média foi {:.2f}'.format(cont,media/cont))
print(f'O maior valor foi {maior} e o menor foi {menor}')