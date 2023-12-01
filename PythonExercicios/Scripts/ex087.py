matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = tercol = maiorseg = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if c == 2:
            tercol += matriz[l][c]
        if c == 0:
            maiorseg = matriz[1][c]
        elif matriz[1][c] > maiorseg:
            maiorseg = matriz[1][c]
    print()
print(f'A soma de todos os valores pares é: {spar}')
print(f'A soma dos valores da terceira coluna é {tercol}')
print(f'O maior valor da segunda linha é {maiorseg}')
