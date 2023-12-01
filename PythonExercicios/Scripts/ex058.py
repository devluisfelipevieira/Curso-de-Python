from random import randint
print(".... O computador está escolhendo um número de 0 a 10 .......")
print("------NÚMERO ESCOLHIDO--------")
npc = randint(0,10)
c = 1
escolha = 0
acertou = False
while not acertou:
    escolha = int(input("Qual número você acha que o computador escolheu? "))
    if escolha == npc:
        acertou = True
        if c > 5:
            print("{}? Certa resposta ☻ \nEssa foi a sua \033[31m{}°\033[m tentativa!!!! PARABÉNS!!!".format(escolha,c))
        else:
            print("{}? Certa resposta ☻ \nEssa foi a sua \033[34m{}°\033[m tentativa!!!! PARABÉNS!!!".format(escolha,c))
    elif npc > escolha:
        print('Não, é MAIOR que {} :('.format(escolha))
        c += 1
    else:
        print('Não, é MENOR que {} :( '.format(escolha))


