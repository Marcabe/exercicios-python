numeros = []

for c in range(0, 5):
    while True:
        try:
            n = int(input(f'Digite um valor para a posição {c}: '))

            if n > -9999999 and n < 9999999:
                numeros.append(n)
                break
            else:
                print('Valor fora do limite. Tente novamente.')

        except ValueError:
            print('Valor inválido. Digite apenas números inteiros.')

print('-' * 40)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {max(numeros)} que se encontra na posição {numeros.index(max(numeros))}')
print(f'O menor valor digitado foi {min(numeros)} que se encontra na posição {numeros.index(min(numeros))}')
print('-' * 40)