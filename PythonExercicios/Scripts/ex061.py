print('Gerador de PA')
print('=-='*10)
n = int(input('Qual a o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
fim = n + (9*r)
print(n,end = ' → ')
while n < fim:
    n += r
    print(n,end = ' → ')
print('Acabou')
