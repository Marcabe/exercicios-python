sexo = str
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo [M/F]: '))
    if sexo != 'M' and sexo != 'F':
     print('Sexo invalido. Digite novamente.')
    else:
     print('Sexo aceite.')