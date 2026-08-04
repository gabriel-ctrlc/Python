#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, casseno e tangente desse angulo
from math import radians, sin, cos, tan
ang = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(ang))
print('O angulo de {} tem o SENO {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))







'''print(
'O angulo de {0} tem o SENO de {1}\n' \
'O angulo de {0} tem o COSSENO de {2}\n' \
'P angulo de {0} tem a TANGENTE de {3}'.format(ang, sin(ang), cos(ang), tan(ang)))'''