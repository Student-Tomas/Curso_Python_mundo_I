# Desafio 026: analisar um frase
frase = str(input('Diga uma frase: ')).lower().strip()
print('Essa frase tem {} letras A'.format(frase.count('a')))
print('A primeira ocorrência é na posição {}'.format(frase.find('a')))
print('A última aparição é na posição {}'.format(frase.rfind('a')))





