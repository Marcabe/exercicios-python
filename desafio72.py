numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezasseis','dezassete','dezoito','dezenove','vinte' )

while True:
    n = int(input('Digite um número entre 0 e 20: '))

    if 0 <= n <= 20:
        break

    print('Número inválido. Tente novamente.')

print(f'Você digitou o número {numeros[n]}.')