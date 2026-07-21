num = []
for c in range(0,5):
    n = int(input(f"Digite um valor para adicionar a lista  na posição {c}: "))
    num.append(n)

maior = max(num)
menor = min(num)

print(f"Os vlaores digitados foram {num}")
print(f"O maior valor foi {maior} na posição {num.index(maior)}...")
print(f"O mneor valor foi {menor} na posição {num.index(menor)}...")

