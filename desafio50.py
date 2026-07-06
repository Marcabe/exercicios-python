soma = 0

for c in range(1,7):
    n= int(input('Digite um Número: '))

    if n % 2 == 0:
        soma += n

print('A Soma dos números pares digitados é {}'.format(soma))