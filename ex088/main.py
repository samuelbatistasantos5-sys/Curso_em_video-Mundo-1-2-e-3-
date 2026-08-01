from random import randint

valores = []
print("-"*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print("-"*40)
sorteios = int(input("Quantos sorteios você quer gerar? "))

for c in range(0,sorteios):
    listavazia = []
    while len(listavazia) < 6:
        n = randint(1,61)
        if n not in listavazia:
            listavazia.append(n)
    valores.append(listavazia[:])
    listavazia.clear()

print(f"{f"SORTEANDO {sorteios} JOGOS":-^40}")
for pos, linha in enumerate(valores):
    print(f"Jogo {pos+1}: ", end=" ")
    print(linha)
print(f'{"BOA SORTE":-^40}')

