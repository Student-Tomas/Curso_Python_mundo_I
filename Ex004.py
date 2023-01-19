#tipos primitivos
'''n1 = input('Diga um número: ')
print(type(n1))
n2 = int(input('Diga outro número: '))
print(type(n2))
n3 = float(input('Diga mais um número: '))
print(type(n3))
n4 = int(input('Diga mais outro número: '))
print(type(n4))
n5 = n2 / n4
print(n5)
print(type(n5))'''
# teste do is
n = input('Número ou letra: ')
print('O tipo primitivo de {} é: {}'.format(n, type(n)))
print(type(n))
print('{} é alpha numérico? {}'.format(n, n.isalnum()))
print(n.isalnum())
print('O que foi digitado é somente letras?', n.isalpha())
print(n.isalpha())
print(n.islower())
print(n.istitle())
print(n.isascii())
print('O que foi digitado é somente espaços? ', n.isspace())
print("é um número? ", n.isnumeric())





