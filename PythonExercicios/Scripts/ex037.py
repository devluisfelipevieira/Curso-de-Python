numero=int(input('Escreva um número: '))
escolha=int(input('\033[30mESCOLHA A BASE DE CONVERSÃO:'
                  '\n\033[1;31m1-PARA BINARIO\033[m'
                  '\n\033[1;33m2-PARA OCTAL\033[m'
                  '\n\033[1;34m3-PARA HEXADECIMAL\n'))
if escolha==1:
    print('{} em BINÁRIO é {}'.format(numero,bin(numero)[2:]))
elif escolha==2:
    print('{} em OCTAL é {}'.format(numero,oct(numero)[2:]))
elif escolha==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Escolha não identificada pelo sistema')