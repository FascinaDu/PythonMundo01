n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2)/2
print(f'A sua média foi {media:.1f}')
if media >= 6:
    print('PARABÉNS, você passou!')
else:
    print('Estude mais...')