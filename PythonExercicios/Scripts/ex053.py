f =  str(input('Digite uma frase: ')).strip().upper()
frase = f.split()
junto = ''.join(frase)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto,inverso))
#for c in range(len(junto) - 1, -1, -1):
    #inverso += junto[c]
#print(inverso)
if inverso == junto:
    print('E são palindromos')
else :
    print('E \033[31mNÃO\033[m são palindromos')

