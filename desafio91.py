from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()

for c in range(1, 5):
    jogadores[f'jogador {c}'] = randint(1, 6)

print('Valores sorteados:')

for jogador, valor in jogadores.items():
    print(f'O {jogador} tirou {valor}')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-' * 30)
print('Ranking dos jogadores:')

for posicao, jogador in enumerate(ranking, start=1):
    print(f'{posicao}º lugar: {jogador[0]} com {jogador[1]}')
    sleep(1)
