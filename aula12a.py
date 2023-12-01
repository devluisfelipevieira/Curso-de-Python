n = str(input('Qual é seu nome? '))
nome=n.upper()
if nome == 'FELIPE':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome =='PAULO':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(n))