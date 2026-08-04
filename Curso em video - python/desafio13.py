# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
n1 = float(input('Digite o salario do funcionario: R$ '))
# novo = n1 + (n1 * 15 / 100)
a = n1*0.15
b = n1+a

print('O novo salario é de: R${:.2f}'.format(b))
