# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR
num = int(input('Digite um numero: '))

num2 = num % 2

if num2 == 0:
    print('O numero que voce digitou é par')
else:
    print('O numero que voce digitou é impar')