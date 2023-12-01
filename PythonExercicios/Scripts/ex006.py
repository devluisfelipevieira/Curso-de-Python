n=int(input('Digite um número: '))
print('\033[1;36mPara o número {},\nO dobro é {},\no triplo é {},\ne a raiz é {:.2f}'.format(n,(n*2),(n*3),pow(n,(1/2))))