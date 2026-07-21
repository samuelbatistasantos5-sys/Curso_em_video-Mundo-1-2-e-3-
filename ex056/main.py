idademedia = 0
idadehomemmaisvelho = 0
nomehomemmaisvelho = ""
mulheresmenosdevinte = 0
masc = ['homem', 'macho', 'masculino']
femi = ['mulher', 'femêa', 'feminino']
for c in range(1,5):
    nome = input(f"Qual o nome da pessoa{c}: ")
    idade = int(input(f"Qual a idade da pessoa{c}: "))
    idademedia += idade
    sexo = input(f"Qual o gênero da pessoa{c}: ")
    sexo = sexo.lower()
    if sexo in masc:
        if idade > idadehomemmaisvelho:
            nomehomemmaisvelho = nome

    elif sexo in femi:
        if idade <= 20:
            mulheresmenosdevinte += 1
    else:
        print('Gênero errado')
    
    

print(f"A idade média do grupo é {idademedia/4}")
print(f"O homem mais velho é {nomehomemmaisvelho}")
print(f"{mulheresmenosdevinte} mulher(es) tem menos de 20")