salario = int(input('Qual é seu salário atualmente? '))

if salario <= 1250:
    print(f'Você recebeu um aumento de R${(salario/100)*15:.2f} e agora seu salário é R${(salario/100)*15+salario:.2f}')
else:
    print(f'Você recebeu um aumento de R${(salario/100)*10:.2f} e agora seu salário é R${(salario/100)*10+salario:.2f}')