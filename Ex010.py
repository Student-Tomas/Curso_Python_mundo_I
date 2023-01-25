#Desafio 10: conversão de moedas
dolar = float(input('Quantos dólares vc tem na carteira? '))
cotacao = float(input('Qual a cotação do atual? '))
real = dolar * cotacao
print('O valor de {} dólares equivale hoje a {} reias'.format(dolar, real))
