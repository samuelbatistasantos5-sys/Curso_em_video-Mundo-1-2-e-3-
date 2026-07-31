matriz = [[], [], []]

for c in range(0,9):
    n = int(input("Digite um valor para adicionar na matriz: "))
    if c <= 2:
        matriz[0].append(n)
    if c >2 and c <= 5:
        matriz[1].append(n)
    if c > 5 and c <= 8:
        matriz[2].append(n)

pares = 0
maior = max(matriz[1])
somaterceiracoluna = 0
for linha in matriz:
    for elemento in linha:
        if elemento%2 == 0:
            pares += elemento
    somaterceiracoluna += linha[2]

print('-='*30)
for linha in matriz:
    print(linha)
print('-='*30)      
print(f"A soma de todos os valores pares foi {pares}")
print(f"A soma de todos os valores da terceira coluna foi {somaterceiracoluna}")
print(f"O maior da segunda linha foi {maior}")

