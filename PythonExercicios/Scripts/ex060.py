'''n = int(input('Escolha um número para ser feito o fatorial: '))
f = 1
for c in range(n,0,-1):
    print(c , end = ' ')
    print(' x 'if c > 1 else ' = ',end = '')
    f *= c
print(f)
'''
n = int(input('Escolha um número para ser feito o fatorial: '))
c = n
f = 1
while c > 0:
    #print(c, end = '')
    #print(' x 'if c > 1 else ' = ',end = '')
    f *= c
    c -= 1
print(f)



