nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = float((nota1 + nota2)/2) 

if media < 5.0:
    print(f'A média do aluno foi {media}, por isso ele foi reprovado')

elif media == 5.0 or media < 7.0:
    print(f'A média do aluno foi {media}, por isso ele foi para a recuperação')

else:
    print(f'A média do aluno foi {media}, por isso ele foi aprovado')


