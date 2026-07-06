primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
quantidade = 10
contador = 0
total = 0

while quantidade != 0:

    total += quantidade

    while contador < total:
        print(termo, end=' → ')
        termo += razao
        contador += 1

    print('PAUSA')

    quantidade = int(input(
        'Quantos termos deseja mostrar a mais? '
    ))

print('Progressão finalizada com {} termos mostrados.'.format(total))