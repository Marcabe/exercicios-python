alunos = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    opcao = input('Quer continuar? [S/N] ').strip().upper()[0]

    while opcao not in 'SN':
        opcao = input('Opção inválida. Quer continuar? [S/N] ').strip().upper()[0]

    if opcao == 'N':
        break

print('-' * 40)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 40)

for posicao, aluno in enumerate(alunos):
    print(f'{posicao:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

print('-' * 40)

while True:
    try:
        notas = int(input('Mostrar notas de qual aluno? [999 para parar] '))
    except ValueError:
        print('Valor inválido. Digite apenas o número do aluno.')
        continue

    if notas == 999:
        break

    if 0 <= notas < len(alunos):
        print(f'Notas de {alunos[notas][0]} são {alunos[notas][1]}')
    else:
        print('Aluno não encontrado.')

print('Programa finalizado.')
