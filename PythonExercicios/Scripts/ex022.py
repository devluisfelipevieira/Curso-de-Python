nome=str(input('Digite seu nome completo: ')).strip()
print('EM MAIÚSCULA: {}'.format(nome.upper()))
print('em minúscula {}'.format(nome.lower()))
print('Tamanho: {}'.format(len(nome)-nome.count(' ')))
print('Tamanho do primeiro nome: {}'.format(len(nome.split()[0])))#print(nome.find(' '))

