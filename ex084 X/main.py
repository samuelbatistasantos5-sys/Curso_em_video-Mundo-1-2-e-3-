listadepessoas = []
dados = []
pessoas = 0
while True:
    print(f'{"Cadrastro de pessoa":-^40}')
    nome = input("Digite o nome da pessoa: ")
    peso = int(input("Digite o peso da pessoa: "))
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

maispesasdo = max(listadepessoas)
print(maispesasdo)
print(f"O maior peso foi de {maispesasdo[0]}Kg. Peso de ", end=" ")
for p in listadepessoas:
    if p == maispesasdo[0]:
        print(p[0])


maisleve = min(listadepessoas)
print()
print("-="*30)
print(f"O total de pessoas cadastradas foram {pessoas} pessoas")
