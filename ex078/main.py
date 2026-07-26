numeros = []
for c in range(0,5):
    num = int(input(f"Digite um valor para adicionar a lista  na posição {c}: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print(f"O maior valor é {maior} nas posições", end=" " )
for indice, n in enumerate(numeros):
    if n == maior:
        posicao = indice
        print(f"{posicao}...", end="")

print()

print(f"O maior valor é {menor} nas posições", end=" " )
for indice, n in enumerate(numeros):
    if n == menor:
        posicao = indice
        print(f"{posicao}...", end="")

