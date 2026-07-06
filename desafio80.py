numeros = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if len(numeros) == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Valor adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(numeros):
            if n < numeros[pos]:
                numeros.insert(pos, n)
                print(f'Valor adicionado na posição {pos}.')
                break
            pos += 1
print('-' * 40)
print(f'Os valores digitados em ordem foram: {numeros}')
print('-' * 40)
