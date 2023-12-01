times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bhaia', 'Sport Recife', 'Chapecoense')
print('-='*15)
print(f'Lista de times do Brasileirão 2021: ')
for t in times:
    print(t)
print('-='*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {times[16:20]}')
print('-='*15)
print(f'Times em ordem alfabética: ')
for t in sorted(times):
    print(t)
print('-='*15)
time = str(input('Qual time você quer saber a posição? '))
print('O {} está na {}ª posição'.format(time,times.index(time)+1))
if times.index(time)+1 == 20:
    print('O ultimo Colocado')