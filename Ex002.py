nome = str(input('Qual o seu nome? '))
print('Hello,', nome,'!')
nome=str(input('Qual o seu nome? '))
print('Bom dia, {}!'.format(nome))
# Desafio número dois: pedir o dia, o mês e o ano de nascimento e formatar com uma pergunta afirmativa
dia = (input('Qual o seu dia de nascimento? '))
mes = (input('Qual o seu mês de nascimento? '))
ano = (input('Qual o seu ano de nascimento? '))
print('{}, {}, {}'.format(dia, mes, ano))
print('Você nasceu no dia {}{}, do mês de {}, do ano de {}{}'.format('\033[4;31;40m', dia, mes, ano, '\033[m'))
print('\033[4;31;40mOlá, {}! Você nasceu no dia {}, do mês de {}, do ano de {}\033[m'.format(nome, dia, mes, ano))
