viagem = int(input('Quanto KM é a viagem? '))

if viagem > 200:
    print(f'Sua viagem é longa e ficará R${viagem*0.45:.2f}')
else:
    print(f'Sua viagem é curta e ficará R${viagem*0.50:.2f}')