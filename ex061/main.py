an = int(input("digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
cont = 0
while cont < 10:
    print(an)
    termo = an+razao
    an = termo
    cont += 1
print("Fim")