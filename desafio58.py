from random import randint

n = randint(0,10)
numero=int
contador = 0

print('Vou pensar em um numero entre 0 e 10.')
print('Tente adivinhar...')

while numero != n:
    contador += 1
    numero = int(input('Digite um numero entre 0 e 10: '))
    if numero != n:
        print('Numero errado. Tente novamente.')
    else:
        print('Numero correto. Parabéns!!!')

print(f'Voce precisou de {contador} tentativas.')