a = input ('Digite algo: ')
# O "a" é objeto, ele tem caracteristicas, e realiza funcionalidades, ele tem atributos e metodos
print ('O tipo primitivo desse valor é', type(a))
print ('Só tem espaços ? ', a.isspace())
print ('É um numero ?', a.isnumeric())
print ('É alfabetico ? ', a.isalpha())
print ('É alfanumerico ?', a.isalnum())
print ('Esta em maiusculas ?', a.isupper())
print ('Esta em minuscula ?', a.islower())
print ('Esta capitalizada ?', a.istitle())

# tentar colocar em format sozinho
print ('Tipo {}, tem espaços {}, numero {}, alfabetico {}, alfanumerico{}, maiuscula {}, minuscula {}, capitalizada{}'.format())