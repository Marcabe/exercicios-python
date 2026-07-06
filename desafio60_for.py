n = int(input('Digite um número para calcular o fatorial: '))

fatorial = 1

print('{}! = '.format(n), end='')

for c in range(n, 0, -1):
    print(c, end='')

    if c > 1:
        print(' × ', end='')
    else:
        print(' = ', end='')

    fatorial *= c

print(fatorial)