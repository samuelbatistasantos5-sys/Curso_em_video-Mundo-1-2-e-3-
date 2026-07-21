from random import randint
pontos = 0
jogador_venceu = True
while jogador_venceu == True:
    print("-"*20)
    print("JOGO DE ÍMPAR OU PAR")
    print("-"*20)
    jogador = int(input("Diga um valor: "))
    npc = randint(0, 10)
    while True:
        decidir = input("Você quer [P/i] ").upper()
        if decidir == "P" or decidir == "I":
            break
        else:
            print("resultado inválido")
    resultado = jogador%npc
    parouimpar = ""
    if resultado == 0:
        parouimpar = "PAR"
    else:
        parouimpar = "IMPAR"
    print(f"Você jogou {jogador} e o computador jogou {npc}. Total de {jogador+npc} DEU {parouimpar}")
    if decidir == "P" and parouimpar == "PAR":
        print("Você venceu!")
        jogador_venceu = True
        pontos += 1
    elif decidir == "I" and parouimpar == "IMPAR":
        print("Você venceu!")
        jogador_venceu = True
        pontos += 1
    else:
        print("GAME OVER!!!")
        break

print(f"O jogador fez {pontos} pontos")

