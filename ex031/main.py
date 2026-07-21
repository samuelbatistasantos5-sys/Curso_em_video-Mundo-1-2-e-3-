distancia = float(input('Quantos KM foram pecorridos durante a viagem: '))

if distancia <= 200.0:
    passagem = distancia*0.50
    print(f'Você terá de pagar R$ {passagem} de passagem')
else:
    passagem = distancia*0.45
    print(f'Você terá de pagar R$ {passagem} de passagem')