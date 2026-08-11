# Escreva um programa que faça um computador pensar em um numero inteiro enre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computaodr
# O programa devera escrever na tela se o usuario venceu ou perdeu.
import random

all = random.randint(0, 5)

while True:
    numero = int(input('Adivinhe qual numero Foi gerado de 0 a 5: '))

    if numero == all: 
        print('Parabens, Voce acertou o numero !')
        print('O número gerado foi:', all)
        break
    else:
        print('Você não acertou o número! Tente novamente.')
        print('---')

    print('o numero gerado foi',all)