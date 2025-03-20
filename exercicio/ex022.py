nome = input('Digite seu nome completo: ')

print(f'Nome maiusculo: {nome.upper()}')

print(f'Nome minusculo: {nome.lower()}')

lista = nome.replace(' ', '')
print(f'Tem total de: {len(lista)} letras')

dividido = nome.split()
print(f'O primeiro nome tem: {len(dividido[0])} letras')
