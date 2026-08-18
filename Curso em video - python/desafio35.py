# Desenvolva um porgrama que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar umm triangulo
print("""-=-=-=-=-=-=-=-=-=-=-=-=
Analisador de Triangulos
-=-=-=-=-=-=-=-=-=-=-=-=""")

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')