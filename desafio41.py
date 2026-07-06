from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print('MIRIM')

elif idade <= 14:
    print('INFANTIL')

elif idade <= 19:
    print('JUNIOR')

elif idade <= 20:
    print('SENIOR')

else:
    print('MASTER')

