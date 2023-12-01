n = int(input('Qual tabuada deve ser exibida? '))
m = 1
for c in range(0,10):
    r = n * m
    print('{} X {} = {}'.format(n,m,r))
    m += 1

