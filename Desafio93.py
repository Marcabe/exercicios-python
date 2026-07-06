aproveitamento = dict()
golos = list()

aproveitamento['nome'] = input('Nome: ')
jogos = int(input('Quantos jogos: '))

for c in range(1, jogos + 1):
    gol = int(input(f'Golos no jogo {c}: '))
    golos.append(gol)

aproveitamento['golos'] = golos
aproveitamento['total'] = sum(golos)
aproveitamento['media'] = aproveitamento['total'] / jogos

print('-' * 30)
print(aproveitamento)
print('-' * 30)

for k, v in aproveitamento.items():
    print(f'{k}: {v}')

print('-' * 30)
print(f'O jogador {aproveitamento["nome"]} jogou {jogos} partidas.')

for i, g in enumerate(golos):
    print(f'Na partida {i + 1}, fez {g} golos.')

print(f'Foi um total de {aproveitamento["total"]} golos.')
print(f'A média de golos por jogo foi de {aproveitamento["media"]:.2f} golos.')