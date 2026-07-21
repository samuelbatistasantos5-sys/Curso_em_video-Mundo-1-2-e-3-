maispesado = 0
menorpeso = 0
for c in range(1, 6):
    peso = float(input("Digite seu peso "))
    if c == 1:
        maispesado = peso
        menorpeso = peso
    else:
        if peso > maispesado:
            maispesado = peso
        if peso < menorpeso:
            menorpeso = peso

print(f"O maior peso é {maispesado}")
print(f"E o menor peso é {menorpeso}")
