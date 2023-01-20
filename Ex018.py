# Desafio 018: seno, cosseno e tangente de um ângulo
import math
ang = float(input('Diga um angulo em graus: '))
had = math.radians(ang)
sen = math.sin(had)
cos = math.cos(had)
tang = math.tan(had)
print('O ângulo de {} tem seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(ang, sen, cos, tang))

