r1 = float(input('Digite o comprimento do primeiro segmento '))
r2 = float(input('Digite o comprimento do segundo segmento '))
r3 = float(input('Digite o comprimento do terceiro segmento '))

if r1 + r2 >= r3 and r3 + r2 >= r1:
    print('Você pode fornar um triângulo com esses três segmentos')
    if r1 == r2 and r2 == r3:
        print('Esse é um triângulo EQUILÁTERO')

    elif r1 == r2 and r2 != r3 or r3 == r2 and r2 != r1 or r1 == r3 and r3 != r2 :
        print('Esse é um triângulo ISÓSCELES')

    else:
        print('Esse é um triângulo ESCALENO')


else:
    print('Você não pode fornar um triângulo com esses três segmentos')