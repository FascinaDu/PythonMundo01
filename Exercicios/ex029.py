vel = int(input('Qual é a velocidade do carro? '))

if vel > 80:
    print(f'Você ultrapassou o limite e foi multado em R${(vel-80)*7:.2f}')
else:
    print('Certinho, dirija com segurança!')