soma = 0
valores = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    valores += 1
    soma += n
print(f'a soma dos {valores} valores foi {soma}')
