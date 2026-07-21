n = int(input("Digite o número para saber seu fatorial: "))
n1 = n
cont = n1
while cont != 1:
    cont -= 1
    fatorial = n1*(cont)
    n1 = fatorial
print(f"O fatorial de {n} é {fatorial}")