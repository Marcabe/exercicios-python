numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')
    op = input('Quer continuar? [S/N] ').strip().upper()[0]

    while op not in 'SN':
        op = input('Opção inválida. Quer continuar? [S/N] ').strip().upper()[0]

    if op == 'N':
        break
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
print('-_' * 40)
print(f'Foram digitados os numeros {numeros}')
print(f'Foram digitados os pares: {pares}')
print(f'Foram digitados os impares: {impares}')
print('-_' * 40)