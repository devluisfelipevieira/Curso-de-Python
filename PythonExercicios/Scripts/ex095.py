cod = 0
jogadores = list()
while True:
    jogador = {}
    print('_'*30)
    nome = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {nome} jogou? '))
    gols = []
    for c in range(1,part+1):
        gols.append(int(input(f'    Quantos gols na partida {c}? ')))
    totgols = 0
    for g in gols:
        totgols += g
    jogador = {'cod': cod,'nome': nome, 'gols': gols, 'total': totgols}
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp in 'Nn':
        break
    cod += 1
print('-='*30)
print(f'{"COD "}{"NOME":<15}{"GOLS":<15}{"TOTAL"}')
print('_'*45)
for j in jogadores:
    print('{:^3}{:<15}{:<15}{}'.format(j['cod'],j['nome'],str(j['gols']),j['total']))
while True:
    print('_'*30)
    esc = int(input('Mostrar dados de qual jogador?(999 para) '))
    if esc == 999:
        print('<< VOLTE SEMPRE >>')
        break
    if esc <= len(jogadores)-1:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[esc]["nome"]}')
        for j,g in enumerate(jogadores[esc]["gols"]):
            print(f'No jogo {j+1} fez {g} gols ')
    else:
        print(f'ERRO! Não existe jogador com código {esc}')


