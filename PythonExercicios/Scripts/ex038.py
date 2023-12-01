import math
print('*********Digite dois números para compará-los********')
n1=int(input('Digite o primeiro número: '))
n2=int(input('Agora o outro para comparar com o {}: '.format(n1)))
if n1>n2:
    print('O {} é o maior número'.format(n1))
elif n1<n2:
    print('O {} é o maior número'.format(n2))
else:
    print('Os números tem o mesmo valor')