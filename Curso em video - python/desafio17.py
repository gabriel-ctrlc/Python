#faça um programa que leia um programa que leia o comprimento do cateto oposto e do cateto adjacentede um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)            

#hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))