from time import sleep
n1 = float(input('Dgite um número: '))
n2 = float(input('Dgite outro número: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''O que fazer com osses números?
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
    '''))
    if escolha == 1:
        result = n1 + n2
        print('{} + {} = {}'.format(n1,n2,result))
    elif escolha == 2:
        result = n1 * n2
        print('{} X {} = {}'.format(n1,n2,result))
    elif escolha == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n1 == n2:
            print('Os números são iguais')
        else:
            print('{} é maior que {}'.format(n2,n1))
    elif escolha == 4:
        n1 = float(input('Dgite um número: '))
        n2 = float(input('Dgite outro número: '))
print('Programa Finalizado com sucesso')
print('Desligando')
print('.', end = ' ')
sleep(1)
print('.', end = ' ')
sleep(1)
print('.')
sleep(1)




