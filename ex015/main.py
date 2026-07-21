dias = int(input('Por quantos dias esse carro foi alugado? '))
km = float(input('Qauntos km foi pecorrido durante esse período? '))

valor_diario = dias*60
valor_km = km*0.15
valor_final = valor_diario+valor_km

print(f'O preço diario do aluguel ficou R$ {valor_diario}, e o valor por quilometragem ficou R$ {valor_km}, totalizando no final R$ {valor_final} ')