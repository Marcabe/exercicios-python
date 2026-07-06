from datetime import date

def voto(ano):
    idade = date.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


ano = int(input('Qual o ano de nascimento? '))
print(voto(ano))