numeros = []

while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Número duplicado. Não vou adicionar.')

    op = input('Quer continuar? [S/N] ').strip().upper()[0]

    while op not in 'SN':
        op = input('Opção inválida. Quer continuar? [S/N] ').strip().upper()[0]

    if op == 'N':
        break

print('-' * 40)
print(f'Você digitou os valores: {sorted(numeros)}')
print(f'O maior valor digitado foi {max(numeros)}')
print(f'O menor valor digitado foi {min(numeros)}')
print('-' * 40)
