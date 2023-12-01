nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
if media >= 7:
    sit = 'Aprovado'
elif 5 < media < 7:
    sit = 'Recuperação'
else:
    sit = 'Reprovado'
aluno = {'Nome': nome, 'Média': media, 'Situação': sit}
print('-='*30)
for k,v in aluno.items():
    print(f'  - {k} é igual a {v}')