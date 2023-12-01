print('Gerador de PA')
print('=-='*10)
n = int(input('Qual a o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
termos = 1
quant = 9
fim = n + (quant*r)
print(n,end = ' → ')
while n < fim:
     n += r
     print(n,end = ' → ')
     termos += 1
print('Pausa')
while quant != 0:
    quant = int(input('Quantos termos você quer mostrar a mais? '))
    fim = n + (quant*r)
    while n < fim:
        n += r
        print(n, end=' → ')
        termos += 1
    if quant != 0 :
        print('PAUSA')
print('Processo finalizado com {} termos mostrados.'.format(termos))

