from datetime import datetime
print('_'*30)
ano = int(input('Em que ano você nasceu? '))
idade = datetime.now().year - ano


def voto():
    v = ''
    global idade
    if idade < 16:
        v = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        v = 'VOTO OPCIONAL'
    elif 18 <= idade < 65:
        v = 'VOTO OBRIGATÓRIO'
    return v


print(f'Com {idade} anos: {voto()}')