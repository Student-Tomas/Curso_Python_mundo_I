


# Desafio 030: criar um sistema que diz se um número escolhido é par ou ímpar
num = int(input('Diga um número inteiro: '))
if num % 2 == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é ÍMPAR')

# abaixo foi a forma que usei na primeira vez que fiz o mundo 01 do curso
'''num = int(input('Escolha um número inteiro qualquer: '))
result = num % 2
if result == 0:
    print('O número é {} par'.format(num))
else:
    print('O número {} é impar'.format(num))'''
