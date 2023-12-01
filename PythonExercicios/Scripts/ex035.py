reta1=int(input("Informe o comprimento da primeira reta:"))
reta2=int(input("Informe o comprimento da segunda reta:"))
reta3=int(input("Informe o comprimento da terceira reta:"))
if reta1+reta2>reta3 and reta1+reta3>reta2 and reta2+reta3>reta1:
    print("Estas três retas podem formar um triângulo")
else:
    print("Estas três retas não podem formar um triângulo")