nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))
media=(nota1+nota2)/2
print('Média = {:.1f}'.format(media))
if media>=7:
    print('\033[1;32;40mAPROVADO!\033[m')
elif 7>media>=5:
    print('\033[1;34;40mRECUPERAÇÃO\033[m')
else:
    print('\033[1;31;40mREPROVADO!\033[m')