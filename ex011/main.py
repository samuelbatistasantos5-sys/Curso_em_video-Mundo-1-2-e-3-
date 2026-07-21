largura = float(input('Quantos metros de largura tem a parede: '))
altura = float(input('Quantos metros de altura tem a parede: '))
area = largura*altura
baldes = int(area/2)

print(f'Sua parede tem {area}m quadrados, e serão necessários {baldes} baldes de tinta para pintar a parede completamente')