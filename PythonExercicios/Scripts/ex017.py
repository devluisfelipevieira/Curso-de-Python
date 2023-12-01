from math import pow,sqrt
co=float(input('Informe o valor do cateto oposto: '))
ca=float(input('Informe o valor do cateto adjacente: '))
h=sqrt(pow(co,2)+pow(ca,2))
print('Sabendo que o Cateto oposto vale {}\nE o cateto ajacente vale {}\nO valor da Hipotenusa é {:.2f}'.format(co,ca,h))