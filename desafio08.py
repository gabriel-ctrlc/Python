# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
n1 = float(input('Uma distancia em metros: '))
cm = n1 * 100
mm = n1 * 1000

print('{} Metros são {:.0f} centimetros, ou {:.0f} milimetros'.format(n1, cm, mm))
