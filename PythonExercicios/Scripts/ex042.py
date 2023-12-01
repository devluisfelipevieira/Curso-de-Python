reta1=int(input("Informe o comprimento da primeira reta:"))
reta2=int(input("Informe o comprimento da segunda reta:"))
reta3=int(input("Informe o comprimento da terceira reta:"))
preto='\033[1;30m'
amarelo='\033[1;33m'
vermelho='\033[1;31m'
para='\033[m'
if reta1+reta2>reta3 and reta1+reta2>reta2 and reta2+reta3>reta1:
    print(preto,'Estas três retas formam um triângulo:',preto)
    if reta1 == reta2 == reta3:
        print(amarelo, 'EQUILATERO', para)
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print(' \033[1;34mISÓSCELES\033[m')
    else:
        print('{}{}{}'.format(vermelho, 'ESCALENO', para))
else:
    print('Estas três retas não podem formar um triângulo')
