numeros = []

while True:
    numeros.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')

    op = input('Quer continuar? [S/N] ').strip().upper()[0]

    while op not in 'SN':
        op = input('Opção inválida. Quer continuar? [S/N] ').strip().upper()[0]

    if op == 'N':
        break

print('-_-' * 40)
print(f'Foram digitados {len(numeros)} numeros')
print(sorted(numeros, reverse=True))
if 5 in numeros:
    print('O valor 5 apareceu na lista')
else:
    print('O valor 5 não foi digitado na lista')
print('-_-' * 40)