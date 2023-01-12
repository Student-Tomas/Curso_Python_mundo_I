viagem = float(input('Qual a distância da viagem? '))
p1 = float(0.5)
p2 = float(0.45)
if viagem <= 200:
    print('Sua viagem custará {:.1f} reais'.format(viagem * p1))
else:
    print('Sua passagem custará {:.1f} reais'.format(viagem * p2))
# também pode ser assim:
viagem = float(input('Distância da viagem: '))
passagem = viagem * p1 if viagem <= 200 else viagem * p2
print('O preço da passagem será {:.2f} reais'.format(passagem))




