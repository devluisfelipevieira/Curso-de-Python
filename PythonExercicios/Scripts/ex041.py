ano=int(input('Digite o seu ano de nascimento para que possamos dizer em qual catégoria você se enquadra:\n '))
idade=2022-ano
if idade<=9:
    categoria='MIRIM'
elif idade>9 and idade<=14:
    categoria='INFANTIL'
elif idade>14 and idade<=19:
    categoria='JUNIOR'
elif idade==20:
    categoria='SÊNIOR'
else:
    categoria='MASTER'
print('Sua categoria é a {}!'.format(categoria))