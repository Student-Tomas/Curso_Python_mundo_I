# Desafio 023 - analisando um número
'''num = str(input('Diga um número de até quatro dígitos: '))
print('Analisando o número {}, temos:'.format(num))
print('Ele tem {} dígitos'.format(len(num)))
print('A unidade é {}'.format(num[3]))
print('A dezena é {}'.format(num[2]))
print('A centena é {}'.format(num[1]))
print('A milhar é {}'.format(num[0]))'''
# da forma acima vai dar erro se o número for menor do que mil, então podemos fazer assim:
'''num1 = int(input('Diga um número de até quatro dígitos: ')) + 1000
num = str(num1)
print('Analisando o número {}, temos:'.format(num))
print('Ele tem {} dígitos'.format(len(num)))
print('A unidade é {}'.format(num[3]))
print('A dezena é {}'.format(num[2]))
print('A centena é {}'.format(num[1]))
print('A milhar é {}'.format(int(num[0]) - 1))'''
# mas da maneira acima vai dar erro quando chegar em 9000 ou mais
# no algorítimo abaixo usaremos int e depois str
'''numero = int(input("Diga um número de até quatro dígitos: ")) + 10000
strnum = str(numero)
print('unidade: {}'.format(strnum[4]))
print('dezena: {}'.format(strnum[3]))
print('centena: {}'.format(strnum[2]))
print('milhar: {}'.format(strnum[1]))'''
# a forma mais complexa seria uasando só int, como segue:
num3 = int(input('Diga um número de até quatro dígitos: '))
u = num3 // 1 % 10
d = num3 // 10 % 10
c = num3 // 100 % 10
m = num3 // 1000 % 10
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')





