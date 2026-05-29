#ordem de precedencia
#1 () parenteses
#2 ** potencia
#3 * / // % multiplicação, divisão, divisão inteira, resto da divisão
#4 + - multiplicação, subtração 
#Exemplo

#print(5 + 3 * 2)
#print(5**2)
#print(5**3)
#print(19//2)
#print(19/2)
#print(356*522)
#print(18%2)
#print(122%3)
#print(4**3)
#print(pow(4,3))
#print(81**(1/2)) Raiz quadrada
#print(25**(1/2))
#print(127**(1/3))
#print('oi' * 5)
#print('=' * 20)
#print('=' * 20)

nome = input('Qual é seu nome ? ')
print('Prazer em te conhecer {:20}!' .format(nome))
n1 = int(input('Um valor '))
n2 = int(input('Outro valor  '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print ('A soma é {},\n o produto é {} \n e a divisão é {}'.format(s, m, d), end=' >>> ')
print('divisão inteira {} e potencia {}'.format(d1, e))
