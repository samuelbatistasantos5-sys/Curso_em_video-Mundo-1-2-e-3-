maisdedezoito = 0
homens = 0
mulheresnovas = 0
while True:
    print("-"*20)
    print("CADASTRE A PESSOA")
    print("-"*20)
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        maisdedezoito += 1
    while True:
        sexo = input("Sexo: [M/F]").upper()
        if sexo in "MF":
            break
    while True:
        continuar = input("Deseja continuar: [S/N]").upper()
        if continuar in "SN":
            break
    if sexo == "M":
        homens += 1
    if sexo == "F":
        if idade < 20:
            mulheresnovas += 1
    if continuar == "N":
        break

print(f"Ao total tem {maisdedezoito} pessoas com mais de 18 anos\n{homens} Homens foram cadastrados\n{mulheresnovas} Mulheres tem menos de 20 anos")
