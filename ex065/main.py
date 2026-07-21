maior = 0
menor = 0
contador = 0
soma_dos_valores = 0
loop = True
while loop == True:
    n = int(input("digite um valor: "))
    soma_dos_valores += n
    while True:
        continuar = input("Deseja continuar? [S/N]").upper()
        if continuar == 'S':
            break
        elif continuar == 'N':
           loop = False
           break
        else:
            pass
    contador += 1
    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
   
print(f"A média dos valores digitados foi {soma_dos_valores/contador}, e o maior valor digitado foi {maior}, e o menor {menor}")