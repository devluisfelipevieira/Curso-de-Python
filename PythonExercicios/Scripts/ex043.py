nome=str(input('Qual seu nome?'))
altura=float(input('informe sua altura, {}:'.format(nome)))
peso=float(input('informe seu peso, {}:'.format(nome)))
imc=peso/(altura**2)
print('Sr {},seu IMC é de {:.1f}'.format(nome,imc))
if imc < 18.5:
    print('É abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('É o peso ideal')
elif 25 <= imc < 30:
    print('É considerado Sobrepeso')
elif 30 >= imc <= 40:
    print('É considerado Obesidade')
else:
    print('\033[1;31mOBESIDADE MORBIDA!')
