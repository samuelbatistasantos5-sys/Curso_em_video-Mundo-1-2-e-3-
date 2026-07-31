matriz = [[], [], []]

for c in range(0,9):
    n = int(input("Digite um valor para adicionar na matriz: "))
    if c <= 2:
        matriz[0].append(n)
    if c >2 and c <= 5:
        matriz[1].append(n)
    if c > 5 and c <= 8:
        matriz[2].append(n)

for linha in matriz:
    print(linha)
