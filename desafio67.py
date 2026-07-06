while True:
    n = int(input('Quer ver a tabuada de qual número? '))

    if n < 0:
        break

    print('-' * 20)

    t = 1

    while t <= 10:
        print(f'{n} x {t} = {n * t}')
        t += 1

    print('-' * 20)

print('Programa encerrado.')