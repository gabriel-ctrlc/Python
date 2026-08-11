# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7.00 por cada Km acima do limite
from random import randint
KM = randint(10, 220)
KM2 = (KM -80) * 7


if KM > 80:
    print('Voce foi multado, Velocidade: ',KM)
    print('A multa ficou no valor de: ',KM2)
else:
    print('Velocidade: ',KM)
    print('Parabens, voce esta no limite da via')