preço = float(input('Digite o valor do produto: '))

print('Escolha umas das opções:')
print('1 para pagamento á vista em dinheiro')
print('2 para pagamento á vista em cartao')
print('3 para pagamento em cartao até 2 x ')
print('4 para pagamento em cartao 3x ou mais ')

opção = int(input('Digite a sua opção'))

if opção == 1:
    print('O preço ficará {}€'.format(preço - (preço * 0.10)))
elif opção == 2:
    print('O preço ficará {}€'.format(preço - (preço * 0.05)))
elif opção == 3:
    print('O preço ficará {}€'.format(preço))
elif opção == 4:
    print('O preço ficará {}€'.format(preço + (preço * 0.20)))