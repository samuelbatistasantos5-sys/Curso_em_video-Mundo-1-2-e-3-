numeros = []

for c in range(0, 5):
    num = int(input("Digite o valor a ser adicionado: "))

    if c == 0:
        numeros.append(num)
        print("Adicionado ao final da lista...")
    else:
        for indice, n in enumerate(numeros):
            if num <= n:
                numeros.insert(indice, num)
                print(f"O valor foi adicionado na posição {indice}...")
                break
                
        else:
            numeros.append(num)
            print("Adicionando ao final da lista...")




print(numeros)