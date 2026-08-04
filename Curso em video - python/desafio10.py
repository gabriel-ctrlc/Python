# Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos Dólares ela pode comprar
# Considere U$1,00 = 3,27
n1 = float(input('Digite o saldo da carteira: '))

a = n1/3.27

print('Seu saldo de R${} é igual a: U${:.2f}'.format(n1, a))
