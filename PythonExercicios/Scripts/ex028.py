import random
print(".... O computador está escolhendo um número de 1 a 5 .......")
print("------NÚMERO ESCOLHIDO--------")
n=[1,2,3,4,5]
npc=random.choice(n)
escolha=int(input("Qual número você acha que o computador escolheu? "))
if escolha == npc:
    print("{}? Certa resposta XD !!!! PARABÉNS!!!".format(escolha))
else:
    print("{}? Resposta errada :( . A resposta certa era {}. Mais sorte da proxima vez".format(escolha,npc))