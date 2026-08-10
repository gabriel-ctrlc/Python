# Faça um programa que leia uma frase pelo teclado e mostra:
 # Quantas vezes aparece a letra"a"
 # Em qual posição ela aparece a primeira vez
 # Em que posição ela aprece a ultima vez.

frase = str(input('Digite uma frase: '))

frase = frase.lower().strip()
frase1 = frase.count('a')
frase2 = frase.find('a') #tem como utilizar .index que refotrna (ValueError se não encontrar o texto)
frase3 = frase.rfind('a')

print('A letra "a" apareceu {} vezes'.format(frase1))
print('A letra "a" aparece a primeira vez na posição {}.'.format(frase2))
print('A letra "a" aparece a ultima vez na posição {}.'.format(frase3))
