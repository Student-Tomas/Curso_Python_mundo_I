# Desafio 12: preço de um produto com desconto de 5%
preço = float(input('Qual o preço atual? '))
desc = float(input('Qual o desconto em percentual? '))
novo_preço = preço * (1 - 5/100)
print('{}{}{}'.format('\033[31m', novo_preço, '\033[m'))


