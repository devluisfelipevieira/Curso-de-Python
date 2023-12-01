n=input('Digite algo: ')
print('O tipo primitivo desse valor é {}{}{}'.format('\033[33m',type(n),'\033[m'))
s='\033[1;30;46m'
n='\033[1;30;41m'
if n.isspace()==True:
    print('Só tem espaços? {}{}'.format(s,'Sim\033[m'))
else:
    print('Só tem espaços? {}{}'.format(n,'Não\033[m'))
if n.isnumeric()==True:
    print('É um número? {}{}'.format(s,'Sim\033[m'))
else:
    print('É um número? {}{}'.format(n,'Não\033[m'))
if n.isalpha()==True:
    print('É alfabético? {}{}'.format(s,'Sim\033[m'))
else:
    print('É alfabético? {}{}'.format(n,'Não\033[m'))
if n.isalnum()==True:
    print('É alfanúmerico? {}{}'.format(s,'Sim\033[m'))
else:
    print('É alfanúmerico? {}{}'.format(n,'Não\033[m'))
if n.isupper()==True:
    print('Está em maiusculas? {}{}'.format(s,'Sim\033[m'))
else:
    print('Está em maiusculas? {}{}'.format(n,'Não\033[m'))
if n.islower()==True:
    print('Está em minusculas? {}{}'.format(s,'Sim\033[m'))
else:
    print('Está em minusculas? {}{}'.format(n,'Não\033[m'))
if n.istitle()==True:
    print('Está capitalizada? {}{}'.format(s,'Sim\033[m'))
else:
    print('Está capitalizada? {}{}'.format(n,'Não\033[m'))
