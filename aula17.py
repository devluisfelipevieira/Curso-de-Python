                                    #Listas
letras = ['a', 'b', 'c']
print(letras)
letras[0] = 'z'#troca o item da posição escolhida
print(letras)
letras.append('i')#adiciona um item
print(letras)
letras.insert(0,'abc')#adiciona um item na posição escolhida no índice
print(letras)
del letras[3]#deleta o item na posição escolhida
print(letras)
letras.pop()#deleta o item na posição desejada ou na última(caso não seja declarado um índice)
print(letras)
letras.remove('z')#remove o item pelo conteudo
print(letras)
if 'b' in letras:
    letras.remove('b')
print(letras)
valores =  list(range(4,11))#cria uma lista de 4 a 11
print(valores)
valores = [8,2,5,4,9,3,0]
valores.sort()#coloca os itens da lista em ordem
print(valores)
valores.sort(reverse=True)#inverte os números da lista
print(valores)
lista = [] # ou lista = list(), cria uma lista vazia
lista.append(5)
lista.append(9)
lista.append(4)
for v in lista:
    print(f'{v}... ',end='')
print('')
for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
valor = list()
for c in range(0,5):
    valor.append(int(input('Digite um valor: ')))
print(valor)


