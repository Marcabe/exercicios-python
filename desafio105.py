def notas(*n, sit=False):
    boletim = dict()

    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['media'] = sum(n) / len(n)

    if sit:
        if boletim['media'] < 5:
            boletim['situacao'] = 'RUIM'
        elif boletim['media'] < 7:
            boletim['situacao'] = 'RAZOÁVEL'
        else:
            boletim['situacao'] = 'BOA'

    return boletim


print(notas(5.5, 2.5, 8.5, sit=True))
