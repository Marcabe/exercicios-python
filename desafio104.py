def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')