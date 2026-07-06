n = int(input('Digite um número para calcular o fatorial: '))

fatorial = 1
contador = n

print('{}! = '.format(n), end='')

while contador > 1:
    print(contador, end=' × ')
    fatorial *= contador
    contador -= 1

print('1 = {}'.format(fatorial))