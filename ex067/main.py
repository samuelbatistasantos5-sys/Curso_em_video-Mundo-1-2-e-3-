while True:
    n = int(input("Digite o valor para saber sua tabuada: "))
    if n < 0:
        break
    for c in range(1,11):
        tabuada = n*c
        print(f"{n} x {c} = {tabuada}")
    
print("Tabuada finalizada. Volte sempre!")