#ordem de precedencia
#1 () parenteses
#2 ** potencia
#3 * / // % multiplicação, divisão, divisão inteira, resto da divisão
#4 + - multiplicação, subtração 
#Exemplo

#print(5 + 3 * 2)        # Primeiro é feita a multiplicação (3 * 2 = 6) e depois a soma (5 + 6 = 11).

#print(5**2)             # O operador ** representa potência. 5 elevado a 2 = 25.

#print(5**3)             # 5 elevado a 3 (5 × 5 × 5) = 125.

#print(19//2)            # // faz a divisão inteira, descartando a parte decimal. Resultado: 9.

#print(19/2)             # / faz a divisão comum. Resultado: 9.5.

#print(356*522)          # Multiplica 356 por 522.

#print(18%2)             # % retorna o resto da divisão. 18 dividido por 2 tem resto 0.

#print(122%3)            # Resto da divisão de 122 por 3. Resultado: 2.

#print(4**3)             # 4 elevado a 3 = 4 × 4 × 4 = 64.

#print(pow(4,3))         # A função pow() também calcula potência. É equivalente a 4**3.

#print(81**(1/2))        # Calcula a raiz quadrada de 81. Resultado: 9.0.

#print(25**(1/2))        # Calcula a raiz quadrada de 25. Resultado: 5.0.

#print(127**(1/3))       # Calcula aproximadamente a raiz cúbica de 127.

#print('oi' * 5)         # Repete a string "oi" cinco vezes. Resultado: "oioioioioi".

#print('=' * 20)         # Repete o caractere "=" vinte vezes, criando uma linha.

#print('=' * 20)         # Mesmo resultado da linha anterior.

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
