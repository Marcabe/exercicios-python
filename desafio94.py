pessoas = []
mulheres = []
soma_idades = 0

while True:
    pessoa = dict()

    pessoa['nome'] = input('Nome: ').strip().upper()
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()

    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('Erro. Sexo [M/F]: ').strip().upper()

    pessoa['idade'] = int(input('Idade: '))

    soma_idades += pessoa['idade']
    pessoas.append(pessoa.copy())

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

    opcao = input('Quer continuar? [S/N] ').strip().upper()

    while opcao not in 'SN':
        opcao = input('Erro. Quer continuar? [S/N] ').strip().upper()

    if opcao == 'N':
        break

media_de_idades = soma_idades / len(pessoas)

print('-' * 40)
print(f'O grupo tem {len(pessoas)} pessoas.')
print(f'A média de idades é {media_de_idades:.2f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}')

print('Pessoas acima da média de idade:')

for pessoa in pessoas:
    if pessoa['idade'] > media_de_idades:
        print(f"Nome: {pessoa['nome']}, Sexo: {pessoa['sexo']}, Idade: {pessoa['idade']}")