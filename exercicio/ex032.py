ano = int(input('Me diga um ano e direi se é bissexto: '))

resto = ano % 4
if resto == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')