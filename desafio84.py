princ = []
temp = []
maior = menor = 0

while True:
    princ.append(input('Nome: '))
    princ.append(float(input('Peso: ')))

    if len(temp) == 0:
        maior = menor = princ[1]
    else:
        if princ[1] > maior:
            maior = princ[1]

        if princ[1] < menor:
            menor = princ[1]

    temp.append(princ[:])
    princ.clear()

    op = input('Quer continuar? [S/N] ').strip().upper()[0]

    while op not in 'SN':
        op = input('Opção inválida. Quer continuar? [S/N] ').strip().upper()[0]

    if op == 'N':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(temp)} pessoas.')

print(f'O maior peso foi de {maior} kg. Peso de:', end=' ')
for p in temp:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')

print()

print(f'O menor peso foi de {menor} kg. Peso de:', end=' ')
for p in temp:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

print()
print('-=' * 30)