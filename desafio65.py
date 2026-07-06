contador = 0
soma = 0
opcao = ''

while opcao != 'N':
    n = int(input('Digite um número: '))

    soma += n
    contador += 1

    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    opcao = input('Quer continuar? [S/N] ').strip().upper()

media = soma / contador

print('Foram digitados {} números.'.format(contador))
print('A média dos números é {:.2f}.'.format(media))
print('O maior número digitado foi {}.'.format(maior))
print('O menor número digitado foi {}.'.format(menor))
