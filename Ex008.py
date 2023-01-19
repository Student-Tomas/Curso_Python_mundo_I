# Desafio 08: passar de metros para milímetros e centimetros
valor = float(input('Qual o valor em metros? '))
cm = valor * 100
mm = valor * 1000
print('O valor de {} metros equivale a {} em cm e a {} em mm'.format(valor, cm, mm))

# colocando cores de uma forma diferente
print(f'A medida de \033[31m{valor}\033[m em metros equivale a \033[33m{cm}\033[m em centímetros')


