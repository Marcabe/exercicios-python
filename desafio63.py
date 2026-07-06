quantidade = int(input('Quantos termos deseja mostrar? '))

primeiro = 0
segundo = 1
contador = 0

print('Sequência de Fibonacci:')

while contador < quantidade:
    print(primeiro, end=' → ')

    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo

    contador += 1

print('FIM')