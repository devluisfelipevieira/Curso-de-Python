palavras = ('aprender', 'programar', 'linguagem',
           'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra \033[34m{p.upper()}\033[m temos', end = ' ')
    for letra in p:
        if letra in 'aiou':
            print(letra,end = ' ')
