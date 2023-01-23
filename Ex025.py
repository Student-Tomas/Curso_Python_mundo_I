# Desafio 025: descobrir se existe a palavra silva no nome de uma pessoa:
nome = str(input("Qual seu nome completo? ")).strip()
print('Seu nome tem Silva? {}'.format("silva" in nome.lower()))
