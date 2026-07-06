from datetime import date


trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento
trabalhador['idade'] = idade

trabalhador['carteira de Trabalho'] = int(input('Carteira de Trabalho (0 se não tem): '))
if trabalhador['carteira de Trabalho'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação :'))
    trabalhador['Salário'] = float(input('Salário: €'))



for k, v in trabalhador.items():
    print(f'{k} = {v}')