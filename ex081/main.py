num = []

while True:
    n = int(input("digite um valor: "))
    num.append(n)
    sn = " "
    while sn not in 'SN':
        sn = input("Deseja continuar a adicionar valores na lista? [S/N]").upper()
    if sn == "S":
        continue
    else:
        break
print(f"Você digitou os valores: {num}")
print(f"Você digitou {len(num)} elementos")
print(f"A lista em ordem decrescente fica {sorted(num, reverse=True)}")
if 5 in num:
    print("O valor 5 parte da lista")
else:
    print("O valor 5 não parte da lista")

