from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p}')
    while True:
        print(i, end=' ')
        if i == f:
            break
        if i > f:
            i -= p
            if i < f:
                break
        if i < f :
            i += p
            if i > f:
                break
        sleep(0.5)
    sleep(0.5)
    print('FIM!')
    sleep(0.5)
    print('-=' * 20)


print('-='*20)
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
inic = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inic,fim,passo)