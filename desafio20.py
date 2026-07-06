import random
from random import choice

aluno1 =(input('Primeiro aluno:'))
aluno2 =(input('Segundo aluno:'))
aluno3 =(input('Terceiro aluno:'))
aluno4 =(input('Quarto aluno:'))

Nomes =(aluno1,aluno2,aluno3,aluno4)
Ordem = random.sample(Nomes, 4)

print('A Ordem de apresentação será {}.'.format(Ordem))