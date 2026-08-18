# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
n1 = float(input('Preço do produto: R$ '))
# novo = n1 - (n1 * 5 / 100)
a = n1*0.05
b = n1 - a

print('O novo preço do produto com 5% de desconto é: R$ {:.2f}'.format(b))
