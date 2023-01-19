# Desafio 13: aumento de 15% no salário
sal = float(input('Qual o salário atual? '))
aum = float(input('Qual o aumento em percentual? '))
novo_sal = sal * (1 + aum / 100)
print('\033[33mO novo salário será de {}{}{}'.format('\033[31m', novo_sal, '\033[m'))
