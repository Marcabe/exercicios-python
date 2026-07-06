n1 = 0
n2 = 0
opcao = 0

n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))

print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
''')


while opcao != 5:
    opcao = int(input('Qual a opcao? '))
    if opcao == 1:
        print('A soma entre {} e {} dá {}.'.format(n1,n2,n1+n2))
    if opcao == 2:
        print('{} multiplicado por {} é {}.'.format(n1,n2,n1*n2))
    if opcao == 3:
        if n1 > n2:
            print('{} maior que {}.'.format(n1,n2))
        elif n1 < n2:
            print('{} maior que {}.'.format(n2, n1))
        else:
            print('Os dois números são iguais.')
    if opcao == 4:
        n1=int(input('Digite o primeiro numero: '))
        n2=int(input('Digite o segundo numero: '))
    if opcao == 5:
        break
print('Fim do programa')

