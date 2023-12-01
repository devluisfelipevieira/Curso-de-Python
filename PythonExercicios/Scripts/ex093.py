jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for c in range(1,part+1):
    gols.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
for i,c in enumerate(gols):
    print(f'    => Na partida {i+1}, fez {c} gols')
print(f'Foi um total de {jogador["total"]} gols.')
print(f'Aproximadamente {jogador["total"]/part} gols por partida')
