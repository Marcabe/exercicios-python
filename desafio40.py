nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('A sua média é {} . Parabéns foi aprovado!'.format(media))

elif media < 5:
    print('A sua média é de {} . Infelizmente foi reprovado.'.format(media))

else:
    print('A sua média é de {} . Tens de fazer Recuperação.'.format(media))