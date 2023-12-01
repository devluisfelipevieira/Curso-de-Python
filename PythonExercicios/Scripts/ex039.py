ano=int(input('Qual ano você nasceu? '))
idade=2022-ano
if idade==18:
    print('Você precisa se alistar esse ano, procure o orgão público responsalve de sua cidade para ficar em dia com o governo federal')
elif idade<18:
    falta=18-idade
    if falta==1:
        print('Você ainda não tem idade para se alistar, faltam {} ano para você se alistar'.format(falta))
    else:
        print('Você ainda não tem idade para se alistar, faltam {} anos para você se alistar'.format(falta))
else:
    passou=idade-18
    print('Já passou {} anos do seu ano de alistamento!'.format(passou))

