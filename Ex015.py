# Desafio 015: conta do aluguel de um carro
dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km foram rodados? '))
pd = 60
pk = 0.15
total = (dias * pd) + (km * pk)
print('O total a pagar é de {}{:.2f}{}'.format('\033[31m', total, '\033[m'))


