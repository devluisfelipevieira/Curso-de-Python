maior = 0
menor = 0
for c in range(1,6):
    pessoa = float(input('Qual o peso da {}° pessoa? '.format(c)))
    if c == 1:
        maior = pessoa
        menor = pessoa
    else:
        if menor < pessoa:
            menor = pessoa
        if maior > pessoa:
            maior = pessoa
print('O maior peso é o {}'.format(maior))
print('O menor peso é o {}'.format(menor))
