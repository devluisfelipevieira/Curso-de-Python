cont = 1
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input('Ano de nascimento da {}º pessoa: '.format(cont)))
    idade = 2022 - ano
    cont +=1
    if idade >= 21:
        maior +=1
    else:
        menor +=1
print('{} atingiram a maioridade e {} não atingiram ainda'.format(maior,menor))