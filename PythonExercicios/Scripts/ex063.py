print('Sequência de Fibonacci')
print('_'*30)
n = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
print('-='*15)
print(n1, end = ' → ')
while n > 1:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    n -= 1
    print(n1, end = ' → ')
print('FIM')