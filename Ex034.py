sal = float(input('Qual o salário? '))
if sal > 1250:
    print('O novo salário será de {}'.format(sal*(1+0.1)))
else:
    print('O novo salário será de {}'.format(sal*(1+0.15)))


