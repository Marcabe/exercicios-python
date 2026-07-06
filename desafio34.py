salario = float(input('Digite o seu salario: '))
if salario > 1250:
    print('O seu salário será {}€'.format(salario + (salario*10)/100))
else:
    print('O seu salário será {}€'.format(salario + (salario*15)/100))