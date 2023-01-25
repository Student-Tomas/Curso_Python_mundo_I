# Desafio 027: dizer qual o primeiro e o último nome de alguém:
nome = str(input('Qual o seu nome completo?: ')).strip()
# esse exercício pode ser feito com listas, mas ainda não aprendemos elas até aqui.
lista = nome.split()
print(lista)
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(lista[len(lista)-1]))



