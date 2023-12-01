'''filme = dict() #Ou filme = {}
filme['titulo'] = 'Star Wars'
filme['ano'] = '1977'
filme['Diretor'] = 'George Lucas'
print(filme)
print(filme.keys()) #Mostra o nome de cada Key
print(filme.values()) #Mostra o valor dentro de cada Key
print(filme.items()) #Mostra o nome de cada Key e o valor dentro dela
for k,v in filme.items():
    print(f'O {k} é {v}')
filme['titulo'] = 'Spider Man'
print(filme)'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'{k}: {v}',end=' ')
    print()
