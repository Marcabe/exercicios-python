from random import choice

lista = ['Pedra', 'Papel', 'Tesoura']
resultado = choice(lista)
escolha = input('Pedra, Papel ou Tesoura ?')

print(resultado)

if escolha == resultado :
    print('Empate')
elif escolha == 'Papel' and resultado == 'Pedra':
    print('Você ganhou')
elif escolha == 'Papel' and resultado == 'Tesoura':
    print('Computador ganhou')
elif escolha == 'Pedra' and resultado == 'Papel':
    print('Computador ganhou')
elif escolha == 'Pedra' and resultado == 'Tesoura':
    print('Você ganhou')
elif escolha == 'Tesoura' and resultado == 'Pedra':
    print('Computador ganhou')
elif escolha == 'Tesoura' and resultado == 'Papel':
    print('Você ganhou')