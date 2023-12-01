n=input('Digite uma frase: ').lower().strip()
print('\033[33mA letra "a" aparece {} vezes na frase '.format(n.count('a')))
print('A primeira vez a letra "a" aparece é na {}° posição'.format(n.find('a')+1))
print('A última vez que o "a" aparece é na {}° posição'.format(n.rfind('a')+1))