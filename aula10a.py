n1 = float(input("Digite a primeira nota: "))
n2= float(input("Digite a segunda nota: "))
m=(n1+n2)/2
print("Sua média foi {}".format(m))
if m>=7:
    print("É uma acima da Média, Parabéns!")
if m>=6 and m<7:
    print("É uma nota na média, Bom")
else:
    print("Sua nota está abaixo da média, estude mais")
