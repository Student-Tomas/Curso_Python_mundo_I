# analisando um nome completo
nome = str(input("Qual o seu nome completo? ")).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(" ", ""))))
# também pode ser feito assim:
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(" ")))
nome1 = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome1[0], len(nome1[0])))
# também pode ser feito assim:
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome1[0], nome.find(" ")))








