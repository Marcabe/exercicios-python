from random import randint

jogos = int(input('Quantos jogos quer que eu sorteie? '))

for c in range(0, jogos):
    jogo = []

    while len(jogo) < 6:
        numero = randint(1, 60)

        if numero not in jogo:
            jogo.append(numero)

    jogo.sort()

    print(f'Jogo {c + 1}: {jogo}')
print('-' * 30)
print(f'Sorteado {jogos} jogos. Boa Sorte')
print('-' * 30)




