frase = input("Digite uma frase: ")
frase = frase.lower()
frase = frase.replace(" ", "")

normal = frase
invertida = ""

for c in range(len(frase) -1, -1, -1):
    invertida = invertida+frase[c]
print(f"O iverso de {normal} é {invertida}")
if normal == invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

