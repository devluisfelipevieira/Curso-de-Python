r = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1,11):
        r = n * c
        print(f'{n} X {c} = {r}')
    m = 1
print('PROGRAMA TABUADA ENCERRADO, volte sempre!')