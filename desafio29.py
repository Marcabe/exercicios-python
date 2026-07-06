velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('multa de {}€'.format((velocidade - 80) * 7))
else:
    print('sem multa')