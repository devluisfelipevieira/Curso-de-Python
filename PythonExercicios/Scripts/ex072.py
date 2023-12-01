ne = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze','treze', 'quatorze', 'quinze','dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end = '')
    print(f'Você digitou o número \033[31m{ne[n-1]}\033[m')
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
        if continuar[0] == 'N' or continuar[0] == 'S':
            break
        print('Não entendi!')
    if continuar[0] == 'N':
        break