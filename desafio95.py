jogadores = []

while True:
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

    jogadores.append(aproveitamento.copy())

    opcao = input('Quer continuar? [S/N] ').strip().upper()[0]

    while opcao not in 'SN':
        opcao = input('Opção inválida. Quer continuar? [S/N] ').strip().upper()[0]

    if opcao == 'N':
        break

print('-' * 50)
print(f'{"COD":<5}{"NOME":<15}{"GOLOS":<20}{"TOTAL":<5}')
print('-' * 50)

for i, jogador in enumerate(jogadores):
    print(f'{i:<5}{jogador["nome"]:<15}{str(jogador["golos"]):<20}{jogador["total"]:<5}')

print('-' * 50)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))

    if busca == 999:
        break

    if 0 <= busca < len(jogadores):
        print(f'Levantamento do jogador {jogadores[busca]["nome"]}:')
        for i, gol in enumerate(jogadores[busca]['golos']):
            print(f'No jogo {i + 1}, fez {gol} golos.')
    else:
        print('Jogador não encontrado.')

print('Programa finalizado.')