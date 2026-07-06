alunos = []

while True:
    aluno = dict()

    aluno['nome'] = input('Digite o nome do aluno: ')
    aluno['media'] = float(input('Digite a média do aluno: '))

    if aluno['media'] >= 5:
        aluno['situacao'] = 'Aprovado'
    else:
        aluno['situacao'] = 'Reprovado'

    alunos.append(aluno.copy())

    opcao = input('Quer continuar? [S/N] ').upper().strip()[0]

    if opcao == 'N':
        break

print('-' * 30)

for aluno in alunos:
    print(f"{aluno['nome']} tirou média {aluno['media']} e está {aluno['situacao']}.")



