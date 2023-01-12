vel = int(input('Qual a velocidade registrada? '))
if vel <= 80:
    print('Tenha uma boa viagem!')
else:
    print('Você foi multado!')
    print('Sua multa será de {} reais'.format(((vel)-80)*7))
