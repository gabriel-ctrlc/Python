frase = 'Curso em video Python' #ocupa 21 espaços na memoria

#Fatiamento
frase[9] #ele idenfica somente o caracter 9 que é a letra V, o python diferencia maiusculo de minusculo
frase[9:13] #range, vai do 9 até o 13 incluindo o 9 e removendo o 13
frase[9:21] #fatia até o 21 cortando o 21 selecionando até o 20
frase[9:21:2] #começa o 9 para no 21, pulando de 2 em 2
frase[:5] #quando omito o inicio ele começa pelo caracter 0, excetuando a letra de posição 5
frase[15:] #indica para o python que quero do inicio de posição 15 até o final que no caso é 20
frase[9::3] #começa da posição 9 até o final e pulando de 3 em 3 casas

#Análise
len(frase) #comprimento
frase.count('o') #contagem da quantidade de o minusculo
frase.count('o',0,13) #ele considera do 0 até 12 não incluindo o 13 tendo somente uma letra 'o'
frase.find('deo') #ele vai me dizer quantas vezes encontrou 'deo' ele diz em que momento começou o 'deo' nesse caso foi na posição 11
frase.find('android') #ele retorna o valor -1, significa que essa função não encontrou 'android'
'Curso' in frase #ele vai escrever na tela se o valor for encontrado, retornando para mim true

#Transformação: Uma linha de string é imutavel mas é possivel mexer nelas através de metodos
frase.replace('Python','Android') #ele procura por 'python' e substitui por 'android'
frase.upper() #upper significa para cima, o que ja for maiusculo ele mantem, o que não for ele troca para maiusculo
frase.lower() #lower significa para baixo, o que for minusculo ele mantem, o que não for ele troca para minusculo
frase.capitalize() #pega a string completa coloca todas em minusculo e a primeira letra troca para maiusculo
frase.title() #ele analisa quantas palavras tem na string, pelas posições dos espaços, e faz o captalize com cada palavra
frase2 = '   Aprenda Python  '
frase2.strip() #remove todos espaços sem utilização, os primeiros e os ultimos
frase2.rstrip() #muitas funcionalidades tem a variação r de rigth(direita), nesse caso ele só remove os ultimos espaços
frase2.lstrip() #remove os espaços da esquerda l de left(esquerda)

#Divisão
frase.split() #ele cria divisão entre os espaços, onde as palavras recebe indexação nova, ele divide uma string em uma lista, onde cada elemento é separado pelo seu splitador

#Junção
'-'.join(frase) #junta todos elementod de frase e utiliza '-' como separador podendo utilizar espaço ou outro caracter para junção

print(frase[:13])

print("""Welcome! Are you completely new to programing?
abount why and how to get started with ppython. fortunately
an experienced programmer in any programming languange
(whatever it may be) can pick up python very quickly.""")