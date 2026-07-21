a = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaço? {a.isspace()}')
print(f'É númerico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Ésta em maiúsculo? {a.isupper()}')
print(f'Ésta em minúsculo? {a.islower()}')
print(f'Ésta capitalizada? {a.istitle()}')


