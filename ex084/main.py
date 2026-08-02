listadepessoas = []
dados = []
pessoas = 0
while True:
    print(f'{"Cadrastro de pessoa":-^40}')
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso da pessoa: "))
    dados.append(nome)
    dados.append(peso)
    listadepessoas.append(dados[:])
    dados.clear()
    pessoas += 1
    sn = " "
    while sn not in "SN":
        sn = input("Deseja continuar? [S/N] ").strip().upper()
    if sn == "S":
        continue
    else:
        break

print("-="*30)
print(f"O total de pessoas cadastradas foram {pessoas} pessoas")
maispesado = max(p[1] for p in listadepessoas)
print(f"O maior peso foi {maispesado}Kg. Peso de ", end="")
for p in listadepessoas:
    if p[1] == maispesado:
        print(f"{f"[{p[0]}]"}", end="")

print()

menorpesado = min(p[1] for p in listadepessoas)
print(f"O menor peso foi {menorpesado}Kg. Peso de ", end="")
for p in listadepessoas:
    if p[1] == menorpesado:
        print(f"{f"[{p[0]}]"}", end="")
print()       

