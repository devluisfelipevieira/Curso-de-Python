pessoa = dict()
galera = list()
totidade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
                break
        print('ERRO! digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    totidade += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] '))[0]
        if continuar in 'SsNn':
            break
        print('ERRO! responda apenas S ou N.')
    if continuar in 'Nn':
        break
print('-='*30)
print(f'- O grupo tem {len(galera)} pessoas')
totmulheres = []
mediaidade = (totidade/len(galera))
print(f'- A média de idade é de {mediaidade:5.2f} anos')
print(f'- As mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'],'-',end=' ')
print()
print('-Lista de pessoas que estão acima da média:')
acimamedia = []
for p in galera:
    if p['idade'] > mediaidade:
        acimamedia.append(p)
for p in acimamedia:
    for k,v in p.items():
        print(f'  {k} = {v};',end=' ')
    print()
print()
print('<<ENCERRADO>>')

