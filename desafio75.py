numeros = ()
pares = ()

for c in range(4):
    n = int(input('Digite um número entre 0 e 9: '))

    while n < 0 or n > 9:
        n = int(input('Número inválido. Digite novamente: '))

    numeros += (n,)

    if n % 2 == 0 and n != 0:
        pares += (n,)

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu na posição {numeros.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')

print(f'Foram digitados os seguintes numeros pares {pares}.')

