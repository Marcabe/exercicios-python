f = str(input('Digite uma frase: ')).strip().upper()

for c in range(1):
    if f == f[::-1]:
        print('Palindromo')
    else:
        print('Não é Palindromo')