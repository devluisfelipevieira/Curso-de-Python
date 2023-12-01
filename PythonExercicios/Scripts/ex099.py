from time import sleep
def maior(*n):
    print('Analisando os valores passados...')
    maior = cont = 0
    for c in n:
        print(c, end=' ')
        sleep(0.7)
        if cont == 0:
            maior = c
        else:
            if c > maior:
            maior = c
        cont +=1
    print(f'Foram passados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-='*30)


print('-='*30)
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
