numeros = []

while True:
    num = int(input("Digite o valor a ser adcionado na lista: "))
    numeros.append(num)
    sn = " "
    while sn not in "SN":
        sn = input("Deseja continuar: [S/N]").upper()
    if sn == "S":
        continue
    else:
        break

pares = []
impares = []

for n in numeros:
    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Todos os valores digitados foram: {numeros}")
print(f"Os valores pares foram {pares}")
print(f"Os valores ímpares foram {impares}")