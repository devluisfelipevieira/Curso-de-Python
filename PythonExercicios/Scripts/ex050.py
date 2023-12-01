s = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}° número: '.format(c)))
    cont += 1
    if n % 2 == 0:
        s += n
        cont += 1
print('a soma dos {} numeros pares é: {}'.format(cont,s))


