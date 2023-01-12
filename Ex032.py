'''ano = int(input("Que ano vc quer analisar? "))
if ano % 4 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

    # também pode ser feito assim:
ano = int(input('Qual o ano? '))
resultado = print(f'O ano de {ano} é bissexto') if ano % 4 == 0  else print(f'O ano de {ano} não é bissexto')'''
# ocorre que o ano de 1900 ou 1700 não são bissextos, então temos que acrescentar uma regra para ser mais preciso.
# O ano tem que ser divisível por quatro e não pode ser divisível por 100. Mas se for divisível por 400 será bissexto.
from datetime import date
ano = int(input('Qual o ano? Ou coloque zero para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
#esse primeiro if foi só para analisar o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("o ano de {} é bissexto".format(ano))
else:
    print(f'O ano de {ano} não é bissexto')
