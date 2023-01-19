# Desafio 017: descobrir a hipotenusa
from math import sqrt, hypot
cat1 = float(input('Diga o tamanho da cateto 01: '))
cat2 = float(input('Diga o tamanho do cateto 02: '))
hip = (cat1**2 + cat2**2)**(1/2)
print(hip)

# outro método
teste = pow(cat1, 2) + pow(cat2, 2)
hip_teste = sqrt(teste)
print(hip_teste)

# melhor método
hip3 = hypot(cat1, cat2)
print(hip3)

