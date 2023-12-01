sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe um sexo valido: ')).strip().upper()[0]
print('Okay, {} é valido'.format(sexo))