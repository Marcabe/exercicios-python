casa = float(input('Qual o valor da casa? €'))
salário = float(input('Qual o seu salário? €'))
anos = int(input('Quantos anos deseja pagar? '))

prestação = casa / (anos * 12)
taxa_esforço = (prestação / salário) * 100

print('A sua taxa de esforço é de {:.2f}%'.format(taxa_esforço))

if taxa_esforço <= 30:
 print('o seu emprestimo foi aprovado')
 print('A sua Prestação será de {:.2f}€ mensais'.format(prestação))

else:
    print('o seu emprestimo foi negado')
    print('A sua taxa de esforço é elevada')

