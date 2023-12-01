'''galera = [['João', 21], ['Ana', 33], ['Joaquim',13], ['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
galera = []
dado = []
pode = npode = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 16:
        print(f'{p[0]} tem {p[1]} anos e pode votar ')
        pode +=1
    else:
        print(f'{p[0]} tem {p[1]} anos e NÃO pode votar ')
        npode +=1
print(f'{pode} pessoa(s) podem votar')
print(f'{npode} pessoa(s) NÃO podem votar')

