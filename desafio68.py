from random import randint
import emoji

contador = 0

print('-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-' * 30)

while True:
    n = int(input('Diga um valor de 0 a 10: '))
    opcao = str(input('[P/I] ')) .strip().upper()[0]
    n2 = randint(0, 10)

    if opcao == 'P':
        if (n +n2) % 2 == 0:
            print('Voce acertou!')
            print(emoji.emojize(':face_exhaling:'))
            contador += 1
        else:
            print('Voce errou!')
            print(emoji.emojize(':face_with_tears_of_joy:'))
            print(f'GAME OVER! Voce obteve {contador} vitorias consecutivas!')
            break
    elif opcao == 'I':
        if (n+n2) % 2 == 0:
            print('Voce errou!')
            print(emoji.emojize(':face_with_tears_of_joy:'))
            print(f'GAME OVER! Voce obteve {contador} vitorias consecutivas!')
            print()
            break
        else:
            print('Voce acertou!')
            print(emoji.emojize(':face_exhaling:'))
            contador += 1


    print(f'Voce jogou {n} e o computador {n2}. Total deu {n + n2 }')