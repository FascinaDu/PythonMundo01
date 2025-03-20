print('Dia = R$60 / Km rodado = R$0,15')
km = int(input('Quantos KM você rodou com o carro? '))
dias = int(input('Quantos dias você alugou ele? '))
print(f'Deu um total de R${(km*0.15)+(dias*60):.2f}')