n = int(input('Digite um número: '))

print('Escolha umas das opções:')
print('1 para bináiro')
print('2 para octal')
print('3 para hexadecimal')

opção = int(input('Digite a sua opção'))

if opção == 1:
    print(bin(n)[2:])
elif opção == 2:
    print(oct(n))
elif opção == 3:
    print(hex(n))

