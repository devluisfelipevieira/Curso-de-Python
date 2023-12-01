exp = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está \033[34mCORRETA\033[m!!!')
else:
    print('Sua expressão está \033[31mERRADA\033[m!!!')


