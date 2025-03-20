a = int(input('Fale a 1° reta: '))
b = int(input('Fale a 2° reta: '))
c = int(input('Fale a 3° reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Sim, se forma um triângulo')
else:
    print('Não, não se forma um triângulo')