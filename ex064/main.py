n = 0
soma = n
contador = 0
while n != 999:
    n = int(input("Digite um valor:"))
    if n == 999:
        break
    else:
       soma += n
    contador += 1
print(f"você digitou {contador} números exceto 999, e a soma deles é  {soma}")