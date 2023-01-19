# Desafio 16: mostrar somente a parte inteira de um número real
from math import floor, ceil, trunc
num = float(input('Diga um número real qualquer: '))
print(floor(num))
print(f'A parte inteira do número citado é {floor(num)}')
# arredondando para cima, temos:
print(ceil(num))

# outro método
print(trunc(num))

# mais um método
print(f'{int(num)}')




