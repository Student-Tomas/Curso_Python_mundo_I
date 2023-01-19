# dobro, triplo e raiz quadrada
n1 = int(input('Diga um número: '))
print('O dobro de {} é {}, seu triplo é {}, já a sua raiz quadrada é {:.4f}'.format(n1, n1*2, n1*3, n1**(1/2)))

# Também pode ser feito usando o "pow"
print(pow(n1, 1/2))
