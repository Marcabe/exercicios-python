from time import sleep
def maior(*valores):
    print('-' * 30)
    print('Analisando os valores passados...')

    for valor in valores:
        print(valor, end=' ')
        sleep(0.3)

    print(f'\nForam informados {len(valores)} valores.')

    if len(valores) == 0:
        print('Nenhum valor foi informado.')
    else:
        maior_valor = valores[0]

        for valor in valores:
            if valor > maior_valor:
                maior_valor = valor

        print(f'O maior valor informado foi {maior_valor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()