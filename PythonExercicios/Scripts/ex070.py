print('_'*30)
loja = 'Vieira Marks'
print(f'{loja:^30}')
print('_'*30)
total = 0
maisde1000 = 0
maisbarato = 0
cont = 1
nomemaisbarato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    total += preço
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        nomemaisbarato = nome
    cont +=1
    if preço > 1000:
        maisde1000 += 1
    if continuar == 'N':
        break
print('{:_^30}'.format('FIM DO PROGRAMA'))
print(f'O total de compra foir R${total:.2f}')
print(f'Temos {maisde1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R${maisbarato:.2f}')



