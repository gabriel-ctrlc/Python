# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas letras maiusculas
# O nome com todas minusculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('seu nome em maiuscula é {}',format(nome.upper()))
print('seu nome em minuscula é {}',format(nome.lower()))
print('Seu nome tem ao todo {} letras', format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras', format(nome.find(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')