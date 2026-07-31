numeros = [[], []]

for a in range(1,8):
    n = int(input(f"Digite o {a}° valor para adicionar a lsita: "))
    if n%2 == 0:
        numeros[1].append(n)
    else:
        numeros[0].append(n)

print(f"Os valores pares digitados foram {sorted(numeros[1])}")
print(f"Os valores impares digitados foram {sorted(numeros[0])}")