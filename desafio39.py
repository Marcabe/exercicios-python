from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

if idade < 18:
    print('Ainda não esta na altura de se alistar')
    print('Ainda faltam {} anos'.format(18 - idade))

elif idade == 18:
    print('Esta na altura de se alistar')

else:
    print('Já passou da hora de se alistar')
    print('Ja passou {} anos'.format(idade - 18))



