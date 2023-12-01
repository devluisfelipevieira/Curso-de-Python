galera = list()
dado = list()
maior = 0
menor = 0
nomemaior = []
nomemenor = []
while True:
    resp = ' '
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    while resp not in 'NnSs':
        resp = str(input('Deseja continuar? [S/N]: ')).strip()
    if resp in 'Nn':
        break
for c in galera:
    if c[1] == maior:
        nomemaior.append(c[0])
    if c[1] == menor:
        nomemenor.append(c[0])

print('#'*40)
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de {nomemaior}')
print(f'O menor peso foi de {menor}Kg. Peso de {nomemenor}')




