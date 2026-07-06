def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s).')


nome = input('Qual o nome do jogador? ')
gols = input('Quantos gols? ')

if nome.strip() == '':
    nome = '<desconhecido>'

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)