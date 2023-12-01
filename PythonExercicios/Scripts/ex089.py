from time import sleep
dado = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dado.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"n°":<4}{"NOME":<15}{"MÉDIA":<4}')
print('_'*30)
for i,a in enumerate(dado):
    print(f'{i:<4}{a[0]:<15}{a[2]:<4}')
while True:
    numaluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if numaluno == 999:
        break
    if numaluno <= len(dado) -1:
        print(f'Notas de {dado[numaluno][0]} são {dado[numaluno][1]} ')
    else:
        print(f'Não existe registro de aluno para o número {numaluno}')
print('FINALIZNADO',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print('.',end='')
sleep(0.5)
print()
print('<<< VOLTE SEMPRE >>>')
    


