#um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome delas e escrevendo o nome escolhido

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Qaurto aluno: '))

alunos = [a1, a2, a3, a4]
escolha = random.choice(alunos)

print ('O aluno escolhido foi {}'.format(escolha))