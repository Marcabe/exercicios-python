somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheresjovem = 0

for p in range(1, 5):
    print('----- {} -----'.format(p))
    nome = str(input('Digite o nome : ')).strip()
    idade = int(input('Digite a idade :'))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M' :
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem :
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20 :
        mulheresjovem += 1

mediaidade = somaidade / 4

print('A media das idades é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Exitem {} mulheres com menos de 20 anos'.format(mulheresjovem))