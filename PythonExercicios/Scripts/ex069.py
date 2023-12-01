mais18 = 0
homem = 0
mulhermenos20 = 0
while True:
    print('_'*30)
    print(f'    CADASTRE UMA PESSOA    ')
    print('_' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulhermenos20 += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('='*6,'FIM DO PROGRAMA','='*6)
print(f'total de pessoas com maioridade: {mais18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulhermenos20} mulheres com menos de 20 anos')



