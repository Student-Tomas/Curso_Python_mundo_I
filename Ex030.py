num = int(input('Escolha um número inteiro qualquer: '))
result = num % 2
if result == 0:
    print('O número é {} par'.format(num))
else:
    print('O número {} é impar'.format(num))
