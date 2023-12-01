def area(a,b):
    x = a * b
    print(f'A área de um terreno {a}X{b} é de {x}m² ')


print(' Controle de Terreno')
print('_' * 21)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)

