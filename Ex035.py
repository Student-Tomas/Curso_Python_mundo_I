l1 = float(input('Lado 01:'))
l2 = float(input('Lado 02:'))
l3 = float(input('Lado 03:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('forma triângulo')
else:
    print('não forma triângulo')
