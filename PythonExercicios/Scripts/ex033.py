n1=int(input("informe um número: "))
n2=int(input("informe outro número: "))
n3=int(input("informe outro número: "))
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n2 and n3>n1:
    maior=n3
print("O maior é \033[34m{}\033[m e o menor é \033[31m{}".format(maior,menor))
