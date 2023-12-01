s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        print(c, end = ' ')
        s += c
        cont += 1
print('\n\033[31mA soma de todos os {} multiplos de 3 é {}'.format(cont,s))