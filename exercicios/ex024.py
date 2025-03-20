city = input('Digite o nome da cidade: ')

minus = city.upper()
dividido = minus.split()
print(f'Sua cidade tem Santo no nome? {'SANTO' in dividido[0]}')