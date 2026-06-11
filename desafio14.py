#escreva um programa que converta uma temperatura digitada em °C para °F

c = float(input('Informe a temperatura em °C: '))

f = ((9 * c) / 5) + 32 #ou f = c * 1.8 + 32

print('O valor de °C{} convertido para °F{}'.format(c, f))