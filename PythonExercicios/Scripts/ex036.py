casa=int(input('Qual o valor da casa desejada? '))
renda=int(input('Qual sua renda mensal? '))
anos=int(input(('Em quantos anos você pretende pagar? ')))
prestação=casa/(anos*12)
porc=renda*0.3
if prestação>porc:
    print('Emprestimo negado!')
else:
    print('Você pode comprar a casa em {} prestações de R${:.2f}'.format(anos*12,prestação))