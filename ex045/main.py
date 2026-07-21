from random import randint
print("Seja bem vindo ao jogo de jokempo")

jogada = int(input("Escolha sua jogada \n[1]Pedra \n[2]Tesoura \n[3]Papel \n"))
npc = randint(1,3)
print(npc)


if jogada == npc:
    print("Empate")
elif jogada == 1 and npc == 2:
    print("Você ganhou!!")
elif jogada == 2 and npc == 3:
    print("Você ganhou!!")
elif jogada == 3 and npc == 1:
    print("Você ganhou!!")

else:
    print("Você perdeu!")
    
