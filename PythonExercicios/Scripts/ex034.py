salario=int(input("Qual o seu salário atual? "))
if salario>1250:
    aumento1=salario+salario*0.1
    print("O salário com o aumento de 10% será {} ".format(aumento1))
else:
    aumento2=salario+salario*0.15
    print("O salário com o aumento de 15% será {} ".format(aumento2))
