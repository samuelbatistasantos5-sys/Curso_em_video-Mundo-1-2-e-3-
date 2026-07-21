from math import sin, cos, tan, radians

graus = float(input('Digite o ângulo: '))

conversao = radians(graus)

print(f'O ângulo {graus} graus, tem o seno {round((sin(conversao)), 2)} o cosseno {round(cos(conversao), 2)} e a tangente {round(tan(conversao), 2)}')