real=float(input('Quanto você tem na carteira?R$ '))
dolar=real/5.71
euro=real/6.43
bit=real/272143.66
print('Com R${} você pode comprar {:.2f} dolares\nOu {:.2f} Euros\nOu {:.4f} bitcoins '.format(real,dolar,euro,bit))