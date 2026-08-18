# Ecreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu Salario: R$'))

if salario >= 1250:
    salarioa = salario * 0.10
else:
    salarioa = salario * 0.15

salario = salario + salarioa

print('Seu salario teve um aumento de: {:.2f}'. format(salarioa))
print('O total do seu salario sera: {:.2f}'.format(salario))