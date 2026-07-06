maiores_de_idade = 0
homens = 0
mulheres_jovens = 0

while True:
    print('-' * 30)
    print('   CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))

    sexo = input('Sexo [M/F]: ').strip().upper()

    while sexo not in 'MF':
        sexo = input('Resposta inválida. Sexo [M/F]: ').strip().upper()

    if idade >= 18:
        maiores_de_idade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_jovens += 1

    opcao = input('Quer continuar? [S/N]: ').strip().upper()

    while opcao not in 'SN':
        opcao = input('Resposta inválida. Quer continuar? [S/N]: ').strip().upper()

    if opcao == 'N':
        break

print('-' * 40)
print(f'Tem {maiores_de_idade} pessoas com 18 anos ou mais.')
print(f'Tem {homens} homens cadastrados.')
print(f'Tem {mulheres_jovens} mulheres com menos de 20 anos.')
print('-' * 40)