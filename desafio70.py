somatotal = 0
maiorque100 = 0
nomemaisbarato = ''
precomaisbarato = 0
contador = 0

print('-' * 30)
print('   LOJA SUPER BARATÃO')
print('-' * 30)

while True:
    produto = input('Nome do produto: ').strip()
    valor = float(input('Valor do produto: € '))

    somatotal += valor
    contador += 1

    if valor > 100:
        maiorque100 += 1

    if contador == 1 or valor < precomaisbarato:
        precomaisbarato = valor
        nomemaisbarato = produto

    continuar = input('Quer continuar [S/N]: ').strip().upper()

    while continuar not in 'SN':
        continuar = input('Opção inválida. Quer continuar [S/N]: ').strip().upper()

    if continuar == 'N':
        break

print('-' * 30)
print('       RESUMO DA COMPRA')
print('-' * 30)
print(f'O total da compra foi {somatotal:.2f}€.')
print(f'Nesta compra existem {maiorque100} produtos que custam mais de 100€.')
print(f'O produto mais barato foi {nomemaisbarato},que custou {precomaisbarato:.2f}€.')
print('-' * 30)