primeiro = int(input('Degite o primeiro Termo: '))
razao = int(input('Degite o razao: '))
termo = int(input('Degite o Termo: '))

ultimo = primeiro + (termo) * razao

for c in range(primeiro,ultimo,razao):
    print(c, end=' -> ')

print('FIM')