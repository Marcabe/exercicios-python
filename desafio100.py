from random import randint
from time import sleep

numeros = []


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')

    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(n, end=' ')
        sleep(0.3)

    print('PRONTO!')


def somapares(lista):
    soma = 0

    for valor in lista:
        if valor % 2 == 0:
            soma += valor
            sleep(0.5)

    print(f'Somando os valores pares de {lista}, temos {soma}.')


sorteia(numeros)
somapares(numeros)