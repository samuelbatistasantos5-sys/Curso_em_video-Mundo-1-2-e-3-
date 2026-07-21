velocidade_do_carro = float(input('A que velocidade o carro está andando: ' ))
velocidade_permitida = float(80)

if velocidade_do_carro > velocidade_permitida:
    print('Você está andando a cima da velocidade permitida')
    multa = (velocidade_do_carro - velocidade_permitida)*7.00
    print(f'Você deverá pagar R$ {multa} de multa')

else:
    print('Você está andando na velocidade permitida')