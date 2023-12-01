nota=float(input('Qual foi a primeira nota? '))
nota2=float(input('E a segunda? '))
cores={'vermelho':'\033[31m','azul':'\033[34m','stop':'\033[m'}
media=(nota+nota2)/2
print('A média entre {}{:.1f}{} e {}{:.1f}{} é {}{:.1f}{}'.format(cores['vermelho'],nota,cores['stop'],cores['vermelho'],nota2,cores['stop'],cores['azul'],media,cores['stop']))
