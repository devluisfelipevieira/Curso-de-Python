vel=int(input("Qual a velocidade que o carro está andando? "))
if vel>80:
    print("O condutor deste veículo será multado por exceder a velocidade permitida, que é 80Km/h")
    multa=(vel-80)*7
    print("A multa aplicada será de {}".format(multa))
else:
    print("Esta velocidade é permitida nesta via")