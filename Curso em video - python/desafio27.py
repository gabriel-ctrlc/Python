# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
 # Ex: Ana maria de Souza
 # primeiro = Ana
 # Ultimo = Souza

nome = str(input('Digite seu nome completo: '))

nome = nome.split()

primeira = nome[0]
ultima = nome[-1]

print('Muito prazer em te conhecer!')
print('O primeiro nome é ',primeira)
print('O ultimo nome é ',ultima)