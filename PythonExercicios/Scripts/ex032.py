ano=int(input("Informe o ano para saber se ele é Bissexto: "))
if ano%4==0:
    if ano<2022:
    print("{} Não foi um ano Bi ".format(ano))
else:
    print("Este ano não foi nem será um ano Bissexto")