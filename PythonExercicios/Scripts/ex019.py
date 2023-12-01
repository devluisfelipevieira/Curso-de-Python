import random
n1=input('Qual é o nome do primeiro aluno ?')
n2=input('Qual é o nome do segundo aluno ?')
n3=input('Qual é o nome do terceiro aluno ?')
n4=input('Qual é o nome do quarto aluno ?')
escolhido=[n1,n2,n3,n4]
print(random.choice(escolhido))
