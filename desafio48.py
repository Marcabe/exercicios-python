soma = 0

for c in range(1, 501):
    if c % 3 == 0:
        soma = soma + c

print('A soma de todos os números impares entre 1 e 500 que são multiplos de 3 é {}'.format(soma))