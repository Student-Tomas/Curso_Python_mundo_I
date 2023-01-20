# Desafio 019: escolhas aleatórias
import random
alunos = ['eu', 'tu', 'ele', 'nos']
print(random.choice(alunos))

# De um jeito mais primitivo, temos
al1 = str(input('Aluno 1: '))
al2 = str(input('Aluno 2: '))
al3 = str(input('Aluno 3: '))
al4 = str(input('Aluno 4: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')

