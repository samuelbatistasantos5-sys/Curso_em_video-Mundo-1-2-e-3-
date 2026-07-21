p = int(input("Quantas pessoas são: "))
for c in range(1, p+1):
    sexo = ""
    print(f"----------PESSOA {c}----------")
    while sexo != "M" and sexo != "F":
        sexo = str(input("Qual seu sexo [M/F]").upper())