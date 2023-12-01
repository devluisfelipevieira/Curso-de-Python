from math import sin,cos,tan,radians
angulo=float(input('Informe um ângulo: '))
print('O ângulo {}\nTem o seno {:.2f}\nO cosseno {:.2f}\nE a tangente {:.2f}'.format(angulo,sin(radians(angulo)),cos(radians(angulo)),tan(radians(angulo))))
