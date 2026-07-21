from random import randint
n = randint(0, 10)
contador = 0
acerto = False
print("Tente acertar o número que o computador pensou... ")
while acerto == False:
    jogador = int(input("Seu palpilte... "))
    contador += 1
    if jogador == n:
        print(f"parabéns, você acertou o número sorteado com {contador} tentativas")
        acerto = True
    else:
        if jogador < n:
            print("Tente um número maior...")
        elif jogador > n:
            print("tente um número menor...")
