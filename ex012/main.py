preco = float(input('Informe o valor do produto: '))
desconto = (preco/100)*5
valor_final =float(preco-desconto)

print(f'O preço do produto é R$  {preco}, e com o desconto de 5% ele fica R$ {valor_final}')