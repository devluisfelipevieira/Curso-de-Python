media = 0
somaidade = 0
maioridadehomem = 0
mulhernova = 0
nomevelho = ''
for c in range(1,5):
    print('----- {}° PESSOA ----- '.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulhernova += 1

media = somaidade /4
print('A média de idade do grupo é {} anos'.format(media))
print('{} é o homem mais velho e tem {} anos'.format(nomevelho,maioridadehomem))
if mulhernova = 1:
    print('{} mulher tem menos de 20 anos'.format(mulhernova))
else:
    print('{} mulheres tem menos de 20 anos'.format(mulhernova))




