from random import randint

numeros = ()

for c in range(5):
    sorteado = randint(0, 10)
    numeros += (sorteado,)

print('Os números sorteados foram:', numeros)