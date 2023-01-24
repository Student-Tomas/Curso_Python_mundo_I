# Desefio 028? criar um jogo que faz o usuário tentar acertar o número que o pc escolheu.
import random
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
# a escolha aleatória feita pelo PC também pode ser escrita da forma abaixo:
#escolhido = random.randint(0, 5)
#print(escolhido)
num = int(input('Escolha seu número entre zero e cinco: '))
print('Please, wait...')
from time import sleep
sleep(5)

if num == escolhido:
    print(f'O PC escolheu {escolhido} e vc escolheu {num}.')
    print('Parabéns! Você acertou!!!')
else:
    print(f'O PC escolheu {escolhido} e vc escolheu {num}')
    print('Sorry, Try again later...')



