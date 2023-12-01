v=int(input("Qual a distância de sua viagem(Km)? "))
if v<201:
    preço=v*0.5
    print("Para esta viagem sera cobrado o valor de \033[1;31mR${}".format(preço))
else:
    longa=v*0.45
    print("Como está viagem tem mais de 200 Km's, será cobrado um preço promocional de \033[36mR${}".format(longa))