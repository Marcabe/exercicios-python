n=float(input('Digite a distância da sua viagem em km: '))
if n<=200:
    print('A sua viagem custará {}€'.format(n*0.50))
else:
    print('A sua viagem custará {}€'.format(n*0.45))