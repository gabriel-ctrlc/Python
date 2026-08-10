'''nome = str(input('Qual o seu nome ? '))
if nome == 'Gustavo':
    print('Qe nome lindo voce tem')
else:
    print('Seu nome é tão normla')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m>= 6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS')