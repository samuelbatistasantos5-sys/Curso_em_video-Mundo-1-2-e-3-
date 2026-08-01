alunos = []

while True:
    listavazia = []
    nome = input("Digite o nome do aluno: ").capitalize()
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))      
    listavazia.extend([nome, nota1, nota2])
    alunos.append(listavazia[:])
    listavazia.clear()
    while True:
        sn = input("Desejar adicionar outro aluno: [S/N]").strip().upper()
        if sn in "SN":
            break
    if sn == "N":
        break
print(f"{"No."}" + f"{"Nome":>10}" + f"{"Média":>20}")
print("."*35)
for pos, aluno in enumerate(alunos):
    print(f"{pos}" + f"{aluno[0]:>12}" + f"{round((aluno[1]+aluno[2])/2, 1):>21}")

while True:
    indice = int(input("Deseja ver as notas de que aluno(Digite a posição): "))
    if indice <= len(alunos):
        print(f"Notas do {alunos[indice][0]}: {alunos[indice][1]} e {alunos[indice][2]}")
    else:
        print("Posição incorreta")
    while True:
        sn = input("Deseja continuar: [S/N]").strip().capitalize()
        if sn in "SN":
            break
    if sn == "N":
        break
print(f"{"Fim do programa":.^35}")
