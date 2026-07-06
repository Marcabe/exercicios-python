soma = 0
contador = 0

while True:
    n = int(input('Digite um numero ou 999 para parar: '))
    contador += 1
    if n == 999:
        break
    soma += n

print(f'Foram digitados {contador} numeros e a sua soma da {soma}')
