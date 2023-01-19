'''n = ("oi") * 5
print(n)
x = ('=+') * 50
print(x)
z = ('olá') + ('oi')
print(z)
print('='*20)
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:^20}'.format(nome))
print('Prazer em te conhecer {:>20}'.format(nome))
print('Prazer em te conhecer {:<20}'.format(nome))
print('Prazer em te conhecer {:=^20}'.format(nome))'''
#operadore aritimeticos
'''n1 = int(input('Diga um valor: '))
n2 = int(input('Diga outro valor: '))
print('A soma deles é {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
print('A soma é {}, a multipolicação é {}, a divisão é {}{:.4f}{}'.format(s, m, '\033[0;34;41m', d, '\033[m'))
print('A divisão inteira é {}, e o resto da divisão é {}, já a potencia é {}'.format(di, r, p))
# Tudo na mesma linha
print('A soma é {}, a multipolicação é {}, a divisão é {}{:.4f}{}'.format(s, m, '\033[0;34;41m', d, '\033[m'), end=' ')
print('A divisão inteira é {}, e o resto da divisão é {}, já a potencia é {}'.format(di, r, p))
# Quebrando as linhas
print('A soma é {}, \n a multipolicação é {}, \n a divisão é {}{:.4f}{}'.format(s, m, '\033[0;34;41m', d, '\033[m'))
print('A divisão inteira é {}, \n e o resto da divisão é {}, \n já a potencia é {}'.format(di, r, p))'''

# Desafio número 5
# Crie o sucessor e o antecessor
n1 = int(input('Diga um número: '))
print('O antecessor de {} é {}, já seu sucessor é {}'.format(n1, n1-1, n1+1) ,end=' ')

# dobro, triplo e raiz quadrada
# Desafio 06
print('O dobro de {} é {}, seu triplo é {}, já a sua raiz quadrada é {:.4f}'.format(n1, n1*2, n1*3, n1**(1/2)))

# media
# Desafio 07
n2 = float(input('Nota 01: '))
n3 = float(input('Nota 02: '))
media = (n2 + n3) / 2
print('A média entre {} e {} é {}{}{}'.format(n2, n3 , '\033[41m', media, '\033[m'))



