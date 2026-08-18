#o mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

alunos = [a1, a2, a3, a4]
ordem = random.sample(alunos, k=4)

print ('A Ordem de apresentação será {}'.format(ordem))

'''
ou

shuffle(alunos)
print('A ordem de apresentação será ')
print(alunos)

'''
