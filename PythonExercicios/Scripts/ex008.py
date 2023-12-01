m=float(input('Qual o valor em metros? '))
print('Essa medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m,m/1000,m/100,m/10,m*10,m*100,m*1000))