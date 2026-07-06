n1 = float(input('Qual é o preço do produto? €'))
n2 = int(input('Digite a % de desconto'))
print('O produto que custava {}€, na promoção com desconto de {}% vai custar {}€'.format(n1,n2,(n1*n2)/100))