total = 0
produtos_maior_mil = 0
preco_menor = 0
menor = ""
contador = 0
while True:
    print("-"*15)
    print("CAIXA VIRTUAL")
    print("-"*15)
    produto = input("Digite o produto: ")
    preco = float(input("digite o preço: R$ "))
    total += preco
    if preco >= 1000:
        produtos_maior_mil += 1
    while True:
        continuar = input("Deseja continuar [S/N]").upper()
        if continuar in "SN":
            break
    contador += 1
    if continuar == "N":
        break
    if contador == 1:
        preco_menor = preco
        menor = produto
    else:
        if preco_menor > preco:
            preco_menor = preco
            menor = produto

print("-"*15)
print("FIM DO PROGRAMA")
print("-"*15)
print(f"O Total das compras foi R$ {total}")
print(f"{produtos_maior_mil} produtos custam mais que R$ 1000.")
print(f"O produto mais barato foi {menor} que custa {preco_menor}")
