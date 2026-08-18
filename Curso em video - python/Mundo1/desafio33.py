# Faça um programa que leia tres numeros e mostre qual é maior e qual o menor
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

# Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

# Verificando quem é o maior
maior = a
if b>a and b>c:
    maior  = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maio valor digitado foi {}'.format(maior))