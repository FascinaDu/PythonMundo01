import random

n1 = random.randint(0, 5)
n2 = int(input('Tente adivinhar o número de 0 a 5: '))

if n1 == n2:
    print('Parabéns, você acertou!')
    print(f'O número era {n1}')
elif n2 > 5:
    print('Selecione um número abaixo entre 0 e 5!')
else:
    print('Errou...tente novamente!')
    print(f'O número era {n1}')
