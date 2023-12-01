from datetime import datetime
nome = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
ctps =int(input('Carteira de Trabalho (0 não tem): '))
if ctps != 0:
    contrat = int(input('Ano de contratação: '))
    salario = float(input('Salário: '))
    ficha = {'nome': nome, 'idade': datetime.now().year - nasc, 'ctps': ctps, 'contratação': contrat, 'salário': salario,'aposentadoria': contrat+35-nasc}
else:
    ficha = {'nome': nome, 'idade': datetime.now().year - nasc, 'ctps': ctps}
print('-='*30)
for k,v in ficha.items():
    print(f'  - {k} tem valor {v}')