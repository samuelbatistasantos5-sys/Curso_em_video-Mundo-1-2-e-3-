print("Seja bem vindo")
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
menu = False
while menu == False:
    print('-'*10)
    print("  Menu")
    print('-'*10)
    opcao = int(input("O que deseja fazer: \n[1]Somar\n[2]Multiplicar\n[3]Maior Valor\n[4]Novos números\n[5]Sair "))
    if opcao == 1:
        soma = a+b
        print(f"A soma dos valores é {soma}")
        continuar = input("Deseja continuar [s/n] ".lower())
        if continuar == "s":
            continue
        else:
            break
    elif opcao == 2:
        mult = a*b
        print(f"O resultado da multiplicação é {mult}")
        continuar = input("Deseja continuar [s/n] ".lower())
        if continuar == "s":
            continue
        else:
            break
    elif opcao == 3:
        maior = a
        if a < b:
            maior = b
        print(f"O maior valor {maior}")
        continuar = input("Deseja continuar [s/n] ".lower())
        if continuar == "s":
            continue
        else:
            break
    elif opcao == 4:
        a2 = int(input("Alterar o primeiro valor para qual: "))
        b2 = int(input("Alterar o segundo valor para qual: "))
        a = a2
        b = b2
        print(f"O novos valores são {a} e {b}")
        continuar = input("Deseja continuar [s/n] ".lower())
        if continuar == "s":
            continue
        else:
            break
    elif opcao == 5:
        break
    else:
        continue
print("Fim do programa")