# Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.

nome = str(input('Digite seu Nome: '))

nome = nome.lower()

print('Seu nome tem Silva ?','silva' in nome)