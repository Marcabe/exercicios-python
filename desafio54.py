from datetime import date

maiores = 0
menores = 0
ano_atual = date.today().year

for c in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = ano_atual - ano_nascimento

    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f'{maiores} pessoas já atingiram a maioridade.')
print(f'{menores} pessoas ainda não atingiram a maioridade.')