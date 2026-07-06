print('=' * 10, 'DESAFIO 71', '=' * 10)

valor = int(input('Qual o valor do saque? € '))

nota = 500
total_notas = 0

print('-' * 30)

while valor > 0:

    if valor >= nota:
        valor -= nota
        total_notas += 1

    else:
        if total_notas > 0:
            print(f'{total_notas} nota(s) de {nota}€')

        if nota == 500:
            nota = 200
        elif nota == 200:
            nota = 100
        elif nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        else:
            break

        total_notas = 0

if total_notas > 0:
    print(f'{total_notas} nota(s) de {nota}€')

print('-' * 30)

if valor == 0:
    print('Saque concluído.')
else:
    print(f'Não foi possível entregar os {valor}€ restantes.')