n1 = float(input('Qual é o salário do Funcionário?'))
n2 = int(input('Qual a % de ajuste de salário? '))
print('Um Funcionário que ganhava {}€, com {}% de aumento, passa a receber {}€'.format(n1,n2,(n1*n2/100)+n1))