lanche = ('Hambúrguer', 'Suco', 'Pizza','Pudim','Batata Frita')
# Tuplas são imutáveis
for cont in range(0,len(lanche)):
    if cont == 1:
        print(f'Eu vou beber {lanche[cont]} na posição {cont}')
    else:
        print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for comida in lanche:
    if comida ==  'Suco':
        print(f'Eu vou beber {comida}')
    else:
        print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida},na posição {pos}')

print(sorted(lanche))#coloca a lista em ordem

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(c.index(5,2)) # O .INDEX ACHA A PRIMEIRA VEZ QUE APARECE O ITEM NA TUPLA OU LISTA
pessoa = ('Luis', 19)
del(pessoa)
print(pessoa)
