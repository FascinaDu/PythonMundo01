frase = input('Digite um frase: ')

minus = frase.upper()
contar = minus.count('A')
achar1 = minus.find('A')
achar2 = minus.rfind('A')

print(f'Na sua frase tem {contar} letras "A"')
print(f'O primeiro "A" se encontra em {achar1}')
print(f'O último "A" se encontra em {achar2}')