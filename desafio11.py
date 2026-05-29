# faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidade tinta necessaria para pinta-la
# sabendo que cada litro de tinta, pinta uma area de 2m²
n1 = float(input('Digite a largura: '))
n2 = float(input('Digite a altura: '))

a = n1*n2
t = a/2

print('A area da parede é de: {}m² e a quantidade de tinta necessária é de: {}litros'.format(a, t))
