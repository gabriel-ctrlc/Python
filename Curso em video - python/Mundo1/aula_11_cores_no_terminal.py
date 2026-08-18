# ANSI 

#\033[style;text;back m - primeiro informar qual estilo, segundo qual a cor do texto e terceiro qual a cor de fundo
#\033[0;33;44 m

# codigos de estilo: 0 none, 1 bold, 4 underline, 7 negative,
# codigos de texto: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 ciano, 37 cinza
# codigos de back: 40, 41, 42, 43, 44, 45, 46, 47, mesmo saquencia do texto porém muda o numero

#\033[0;30;41m letra branca e fundo vermelho
#\033[4;33;44m letra amarela e fundo azul
#\033[1;35;43m letra roxo e fundo amarelo
#\033[30;42m letra branca e fundo verde
#\033[m      letra branca e fundo preto, padrão do terminal
#\033[7;30m  letra preta e fundo branco

#print('\033[mOlá, Mundo')


#a = 3
#b = 5
#print('Os valores são \033[32m{}\033[m e \033[34m{}'.format(a, b))


nome = 'Guanabara'
print('Olá, Mundo prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))