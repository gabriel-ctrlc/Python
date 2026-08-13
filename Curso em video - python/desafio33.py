# Faça um programa que leia tres numeros e mostre qual é maior e qual o menor
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))

if valor1 > valor2 and valor3:
    print('O Priemiro numero digitado é o de maior valor')
if valor2 > valor1 and valor3:
    print('O segundo numero digitado é o de maior valor')
if valor3 > valor1 and valor2:
    print('O terceiro numero é o de maior valor')