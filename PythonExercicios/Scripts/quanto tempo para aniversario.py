from datetime import datetime
print('Informe sua data de aniversário em ordem: ')
dia = int(input('Dia: '))
mes = int(input('Mês: ')) * 30
ano = int(input('Ano: ')) * 365
diaat = datetime.now().day
mesat = datetime.now().month * 30
anoat = datetime.now().year * 365
nasc = dia + mes + ano
data = diaat + mesat + anoat
diasanv = (dia + mes + anoat) - data
print(f'faltam aproximadamente {diasanv} dias para seu aniversário')

