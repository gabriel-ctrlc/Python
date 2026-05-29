# faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
# ex 8 antes é 7 depois é 9
n1 = int(input('Digite um numero: '))
a = n1 - 1
b = n1 + 1
print('O valor digitado foi {} seu antecessor é {} seu sucessor é {}'.format(n1, a, b))
