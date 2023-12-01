print('*****TESTE DE NÚMERO PRIMO*****')
n = int(input('Digite o número: '))
somador = 1
contprimo = 0
for c in range (1,n+1):
    primo = n % somador
    somador +=1
    if primo == 0:
        print('\033[31m', end = ' ')
        contprimo +=1
    else:
        print('\033[34m',end = ' ')
    print(c, end = ' ')
print('\n\033[mEste número é divisivel {} vezes'.format(contprimo))
if contprimo == 2:
    print('Este número é primo')
else:
    print('Este númeor NÃO é primo')
