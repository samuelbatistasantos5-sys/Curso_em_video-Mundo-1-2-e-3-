print("="*20)
print("   CAIXA VIRTUAL")
print("="*20)

cedulaciquenta = 0
cedulavinte = 0
ceduladez = 0
cedulaum = 0

contador = 1
dinheiro = int(input("Digite o valor para sacar R$ "))
money = dinheiro

while money != 0:

    if contador == 1:
        calculo1 = money//50
        calculo2 = money%50
        cedulaciquenta += calculo1
        money = calculo2
        print(money)

    elif contador == 2:
        calculo1 = money//20
        calculo2 = money%20
        cedulavinte += calculo1
        money = calculo2
        print(money)

    elif contador == 3:
        calculo1 = money//10
        calculo2 = money%10
        ceduladez += calculo1
        money = calculo2
        print(money)

    elif contador == 4:
        calculo1 = money//1
        calculo2 = money%1
        cedulaum += calculo1
        money = calculo2
        print(money)
    
    else:
        break
    contador += 1


print(f"Total de cédulas de R$ 50,00: {cedulaciquenta}")
print(f"Total de cédulas de R$ 20,00: {cedulavinte}")
print(f"Total de cédulas de R$ 10,00: {ceduladez}")
print(f"Total de cédulas de R$ 1,00: {cedulaum}")

    


