a1 = a2 = a3 = a4 = noves = posicadotres = 0

for c in range(1,5):
    a = int(input("digite um valor: "))
    if c == 1:
        a1 = a
    if c == 2:
        a2 = a
    if c == 3:
        a3 = a
    if c == 4:
        a4 = a
                  
valores = (a1,a2,a3,a4)
print(f"Você digitou os valores {valores}")
      
if 9 in valores:
    noves = valores.count(9)
    print(f"Você digitou o valor nove {noves} vezes")
else:
    print("O valor nove não foi digitado")

if 3 in valores:
    posicadotres = valores.index(3)
    print(f"o valor três aparece primeiro na posição {posicadotres + 1}")
else:
    print("O valor três não foi digitado ")

print(f"os números pares foi", end=" ")
for n in valores:
    if n%2 == 0:
        print(n, end=" ")
        



