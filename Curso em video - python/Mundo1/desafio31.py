# Faça um programa que pergunte a distancia em Km. 
# Calcule o preço da passagem. Cobrando R$0.50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Digite quantos KM voce ira viajar: '))
 
#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 // operador ternario ou if in line

if distancia >= 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50

print(f'O preço da passagem será de: {preco:.2f}')