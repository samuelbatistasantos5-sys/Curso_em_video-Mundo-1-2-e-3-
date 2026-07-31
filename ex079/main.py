valores = []
while True:
    n = int(input("Digite o valor para adicionar na lista: "))
    if n in valores:
        print("Valor já dentro da lista, não vou adicionar")
    else:
        valores.append(n)
        print("Valor adcionado com sucesso")
    sn = input("Deseja continuar: [s/n]").lower()
    while sn not in "sn":
        print("Tente novamente...") 
        sn = input("Deseja continuar: [s/n]").lower()
    if sn == 's':
        continue
    else:
        break
print("-="*15)
print(f"Os valores digitados foram {sorted(valores)}")
print("Fim do pragrama")