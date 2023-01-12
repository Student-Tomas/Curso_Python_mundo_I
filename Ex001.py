print('Hello, World!')
#Desafio 01
#pergunte o nome de uma pessoa e lhe mostre uma mensgem de boas vindas
#já vou colocar cores para treinar
nome = input('Qual o seu nome? ')
print("\033[1;31;45mOlá, {}! Seja bem vindo\033[m".format(nome))
print(f'Olá, {nome}!!! Seja bem vindo!!!')
print('Seja bem vindo, \033[0;35;41m{}\033[m'.format(nome))
print('Seja bem vindo, {}{}{}!'.format('\033[0;30;41m', nome, '\033[m'))
