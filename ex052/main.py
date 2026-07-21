n = int(input("Digite um número para saber se ele é primo: "))
primo = True
for c in range(2,n):
    divisao = n%c
    if divisao == 0:
        primo = False
        break

print(primo)
if primo == True:
    print(f"O número {n} é primo")
else:
    print(f"O número {n} não é primo")
