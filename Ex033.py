num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))
num3 = int(input('Terceiro valor:'))
#lista = [num1, num2, num3]
# para achar o maior número sem usar listas
if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')
#para achar o menor número sem usar listas
if num1 < num2 and num1 < num3:
    print(f'O menor número é {num1}')
elif num2 < num3 and num2 < num1:
    print(f'O menor número é {num2}')
else:
    print(f'O menor número é {num3}')

