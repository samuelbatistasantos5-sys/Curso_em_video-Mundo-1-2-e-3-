nome = input('Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())

dividindo = nome.split()
print(f'O nome cpmpleto sem espaço tem {len(''.join(dividindo))} letras')
print(f'O primeiro nome tem {len(dividindo[0])} letras')