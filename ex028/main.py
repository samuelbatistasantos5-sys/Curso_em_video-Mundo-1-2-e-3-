from random import randint

numero_sorteado = randint(0, 5)
jogada = int(input('Escolha um nùmero de 0 a 5:  '))

if jogada == numero_sorteado:
    print(f'Parabéns, você acertou o número sorteado {numero_sorteado}')
else:
    print(f'Você não acertou o número certo ({numero_sorteado}), tente na pr;oxima')
