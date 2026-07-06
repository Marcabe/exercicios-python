altura = float(input('Digite a sua altura em metros, por exemplo 1.70: '))
peso = float(input('Digite o seu peso em kg: '))

imc = peso / (altura ** 2)

print('O seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')