# Desafio 029: lei a velocidade de um carro e diga se ele foi multado e qual o valor da multa
vel = int(input("Qual a velocidade registrada pelo radar? "))
limite = 80
valor = (vel - limite) * 7
if vel > limite:
    print('Você ultrapassou o limite de velocidade')
   # print(f'O valor da multa será de {valor}')
    print("O valor da multa será de {}{:.2f}{} reais".format('\033[31m', valor, '\033[m'))
else:
    print('\033[32mTenha uma boa viagem!\033[m')

# esse algorítimo foi usado na primeira vez que fiz o mundo 01 do curso:
'''vel = int(input('Qual a velocidade registrada? '))
if vel <= 80:
    print('Tenha uma boa viagem!')
else:
    print('Você foi multado!')
    print('Sua multa será de {} reais'.format(((vel)-80)*7))'''
