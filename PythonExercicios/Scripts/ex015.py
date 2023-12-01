dias=int(input('Quantos dias alugados? '))
km=int(input("Quantos Km's rodados? "))
print('O total a pagar é de R${:.2f}'.format(60*dias+0.15*km))