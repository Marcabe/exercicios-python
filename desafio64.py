n = int(input('Digite um numero: '))

soma = 0
contador = 0

while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um numero: '))

print('A soma de todos os elementos foi de {}'.format(soma))