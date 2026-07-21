an = int(input("digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
total_de_termos = 10
cont = 0
while cont < total_de_termos:
    print(an, end="-")
    termo = an+razao
    an = termo
    cont += 1
    if cont == total_de_termos:
        print("Pausa")
        termos_adicionais = int(input("Quantos termos mais você quer: "))
        if termos_adicionais == total_de_termos:
            pass
        elif termos_adicionais != total_de_termos:
            total_de_termos += termos_adicionais
            continue
        elif termos_adicionais == 0:
            break

print("Fim do programa")



