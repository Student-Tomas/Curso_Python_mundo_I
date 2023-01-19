# Desafio 11: calcular a quantidade de tinta gasta para pintar uma parede.
alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a larguar da parede? '))
area = alt * lar
consumo = float(input('Qual o conusmo de tinta por metro quadrado? '))
gasto = area / consumo
print('Uma parede de {} de altura e {} de larguara vai consumir {} para ser pintada'.format(alt, lar, gasto))
